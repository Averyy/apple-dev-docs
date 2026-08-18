# Using Client Libraries

**Framework**: Apple Ads Platform API

Integrate the Apple Ads Platform API using an Apple-maintained client library instead of a custom HTTP client.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Writing your own integration means owning retry logic, response parsing, and model definitions for every endpoint you call, and keeping all of it correct as the API evolves. A client library takes on that maintenance burden for you, letting your team focus on campaign logic instead of plumbing.

Apple distributes each library through standard, language-specific means, and maintains and versions it alongside the Apple Ads Platform API, so new endpoints, fields, and enumeration values become available through routine dependency updates rather than manual rework. The libraries also handle the OAuth token lifecycle, including requesting and refreshing access tokens, so your application code can focus on calling endpoints rather than managing credentials. Sensible defaults get you running quickly, and extension points let you adapt request handling, logging, and credential management to fit how you built your application.

#### Select a Library

Choose the library that matches your application’s language:

| Language | Repository |
| --- | --- |
| Swift | [`apple-ads-platform-api-swift`](https://developer.apple.comhttps://github.com/apple/apple-ads-platform-api-swift) |
| Python | [`apple-ads-platform-api-python`](https://developer.apple.comhttps://github.com/apple/apple-ads-platform-api-python) |
| Java | [`apple-ads-platform-api-java`](https://developer.apple.comhttps://github.com/apple/apple-ads-platform-api-java) |
| Node.js | [`apple-ads-platform-api-node`](https://developer.apple.comhttps://github.com/apple/apple-ads-platform-api-node) |

#### Get Started

To generate the credentials your application authenticates with, complete the setup steps in [`Implementing OAuth for the Apple Ads Platform API`](implementing-oauth-for-the-apple-ads-platform-api.md) before integrating a client library. Each repository includes a README with installation instructions, authentication setup, and usage examples specific to that language. To install the library and construct a client, refer to the README for your library’s language. For details on the underlying request and response structures the libraries wrap, see [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md).

## See Also

- [Implementing OAuth for the Apple Ads Platform API](implementing-oauth-for-the-apple-ads-platform-api.md)
  Generate a key pair and request an access token to authenticate with the Apple Ads Platform API.
- [Calling the Apple Ads Platform API](calling-apple-ads-platform-api.md)
  Authenticate requests, structure endpoint calls, and interpret responses when using the Apple Ads Platform API.
- [Applying Rate Limits](rate-limits.md)
  Track your remaining quota and pace requests.
- [Advertising Your App on the App Store](journey-app-store-ads.md)
  Set up and launch an App Store campaign, from account verification through keyword targeting to performance reporting.
- [Advertising Your Business on Apple Maps](journey-apple-maps-brand-ads.md)
  Identify your brand, upload creative assets, build location groups, and create campaigns, ad groups, creatives, and ads to promote it on Apple Maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/client-libraries)*