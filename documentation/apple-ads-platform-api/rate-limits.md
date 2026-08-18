# Applying Rate Limits

**Framework**: Apple Ads Platform API

Track your remaining quota and pace requests.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Rate limits exist in the Apple Ads Platform API to avoid latency and other system problems from too many API calls within a limited time. Every response, successful or not, includes a set of rate-limit headers based on the [`IETF RateLimit header fields draft`](https://developer.apple.comhttps://www.ietf.org/archive/id/draft-polli-ratelimit-headers-02.txt), and reports your remaining request quota so your client can pace requests and back off before hitting a `429` rate limit.

#### Read the Rate Limit Headers

The following table details the three header types:

| Header | Type | Description |
| --- | --- | --- |
| `RateLimit-Limit` | integer | The total request quota the API allots to the caller for the current rate-limit window |
| `RateLimit-Remaining` | integer | The number of requests remaining in the current window |
| `RateLimit-Reset` | integer | The number of seconds until the current window resets and `RateLimit-Remaining` returns to `RateLimit-Limit`, as a delta in seconds, not a timestamp, consistent with `Retry-After` |

A response looks like the following:

```None
HTTP/1.1 200 OK
RateLimit-Limit: 100
RateLimit-Remaining: 4
RateLimit-Reset: 37
```

When the server rejects a request with `429` / `rate_limit_exceeded`, the response also includes a `Retry-After` header, giving the number of seconds to wait before the server accepts the next request. Prefer `Retry-After` over `RateLimit-Reset` when both are present on a `429` response because it reflects the exact wait for that rejected request.

#### Implement Rate Limit Handling in a Custom Client

If you call the API directly (rather than through a generated SDK), read the rate-limit headers off every HTTP response your client receives and use them to pace requests. Apply the following pacing rules:

- Before issuing your next request, check `RateLimit-Remaining`. If it’s low, wait roughly `RateLimit-Reset` seconds so the window has a chance to refresh, instead of waiting for a `429`.
- If a request fails with `429`, wait the number of seconds that `Retry-After` specifies (falling back to `RateLimit-Reset`, then to a default) before retrying.
- Double the wait on each consecutive `429`, up to a maximum backoff, such as 16 seconds. After reaching the maximum, don’t increase the wait period between retries.
- Reset your backoff counter back to the minimum wait once a request succeeds.

The following example applies to any custom HTTP client: Read the three headers off the response, throttle proactively, and back off on `429`.

```python
import time
import requests

def call_with_backoff(method, url, max_retries=5, max_backoff=16, **kwargs):
    """Issue an HTTP request against the Apple Ads Platform API, pacing
    requests using the RateLimit-* / Retry-After response headers."""
    wait = 2
    for attempt in range(max_retries):
        response = requests.request(method, url, **kwargs)
        headers = response.headers

        if response.status_code == 429:
            retry_after = headers.get("Retry-After") or headers.get("RateLimit-Reset")
            time.sleep(float(retry_after) if retry_after is not None else wait)
            wait = min(wait * 2, max_backoff)
            continue

        remaining = headers.get("RateLimit-Remaining")
        reset = headers.get("RateLimit-Reset")
        if remaining is not None and reset is not None and int(remaining) < 5:
            time.sleep(int(reset))

        return response

    raise RuntimeError(f"Exceeded {max_retries} retries due to rate limiting")

response = call_with_backoff(
    "GET",
    "https://api.ads.apple.com/v1/campaigns/542317095",
    headers={
        "Authorization": "Bearer {access_token}",
        "X-AP-Context": "adAccountId={adAccountId}",
    },
)
```

#### Implement Rate Limit Handling in a Generated Client

If you use a generated client instead, every method has a `_with_http_info` counterpart that returns a `(data, status_code, headers)` tuple giving you the same access to the rate-limit headers. The logic above applies unchanged. Just read `headers.get(...)` from that tuple rather than from a `requests.Response`, as shown here:

```python
data, status, headers = client.campaigns_id_get_with_http_info(ctx, campaign_id)
print(headers.get("RateLimit-Remaining"))
print(headers.get("RateLimit-Reset"))
```

Apply the same header-aware backoff strategy for every endpoint that returns a `429`, regardless of which HTTP client or SDK you use.

For the full request and response structure reference, see [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md).

## See Also

- [Implementing OAuth for the Apple Ads Platform API](implementing-oauth-for-the-apple-ads-platform-api.md)
  Generate a key pair and request an access token to authenticate with the Apple Ads Platform API.
- [Calling the Apple Ads Platform API](calling-apple-ads-platform-api.md)
  Authenticate requests, structure endpoint calls, and interpret responses when using the Apple Ads Platform API.
- [Using Client Libraries](client-libraries.md)
  Integrate the Apple Ads Platform API using an Apple-maintained client library instead of a custom HTTP client.
- [Advertising Your App on the App Store](journey-app-store-ads.md)
  Set up and launch an App Store campaign, from account verification through keyword targeting to performance reporting.
- [Advertising Your Business on Apple Maps](journey-apple-maps-brand-ads.md)
  Identify your brand, upload creative assets, build location groups, and create campaigns, ad groups, creatives, and ads to promote it on Apple Maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/rate-limits)*