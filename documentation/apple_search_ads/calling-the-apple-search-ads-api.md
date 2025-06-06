# Calling the Apple Search Ads API

**Framework**: Apple Search Ads

Pass your access token in the authorization header of HTTP requests.

#### Overview

Before you can call the API, you need to perform the implementation steps in [`Implementing OAuth for the Apple Search Ads API`](implementing-oauth-for-the-apple-search-ads-api.md).

To call the Apple Search Ads Campaign Management API, pass your access token as `Bearer` in the authorization header of HTTP requests. The `Bearer` value informs the API that the bearer of the token has authorization to access the API and perform specified actions. The following is an example call to the API:

```console
curl "https://api.searchads.apple.com/api/v5/campaigns" \
-H "Authorization: Bearer {access_token}" \
-H "X-AP-Context: orgId={orgId}"
```

|  |  |
| --- | --- |
| `Authorization` | . The authorization value is always `Bearer`. |
| `X-AP-Context` | . The value is your `orgId`.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) : This isn’t a requirement when calling [`Get User ACL`](get-user-acl.md) and [`Get Me Details`](get-me-details.md). |

To return the `userId` and `parentOrgId` of an API caller, use [`Get Me Details`](get-me-details.md).

##### Handle Errors

|  |  |  |
| --- | --- | --- |
| `401` | `unauthorized` | The token is invalid or expired. |
| `403` | `forbidden` | The request requires higher privileges than the access token provides. |

##### Rate Limits

Rate limits exist in the Apple Search Ads Campaign Management API to avoid latency and other system problems from too many API calls within a limited time. For API users that are using automated retry logic in their environments, Apple’s solution is to require the retry logic to increase retry attempts exponentially by seconds. For example, if your default minimum wait time between retries is 2 seconds, the next retry wait time is 4 seconds, and so forth.

Set a maximum exponential backoff time, such as 16 seconds. After reaching the maximum time, don’t increase the wait period between retries.

- If the request fails, wait 2 seconds and retry the request.
- If the request fails, wait 4 seconds and retry the request.
- If the request fails, wait 8 seconds and retry the request.
- If the request fails, wait 16 seconds and retry the request.

## Topics

### Access Control List
- [Get User ACL](get-user-acl.md)
  Fetches roles and organizations that the API has access to.
- [object UserAcl](useracl.md)
  The response to ACL requests.
- [object UserAclListResponse](useracllistresponse.md)
  A container for ACL call responses.
- [Get Me Details](get-me-details.md)
  Fetches details of an API caller.
- [object MeDetail](medetail.md)
  The API caller identifiers.
- [object MeDetailResponse](medetailresponse.md)
  The response from me detail calls.
### Error Responses
- [object ApiErrorResponse](apierrorresponse.md)
  A parent object of the error response body.
- [object ErrorResponseBody](errorresponsebody.md)
  A parent object of the error response.
- [object ErrorResponseItem](errorresponseitem.md)
  The error response details in the response body.
- [object IntegerResponse](integerresponse.md)
  A common integer type response.
- [object VoidResponse](voidresponse.md)
  A default generic null response.

## See Also

- [Implementing OAuth for the Apple Search Ads API](implementing-oauth-for-the-apple-search-ads-api.md)
  Manage secure access to Search Ads accounts.
- [Using Apple Search Ads API Functionality](using-apple-search-ads-api-functionality.md)
  Call endpoints using CRUD methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/calling-the-apple-search-ads-api)*