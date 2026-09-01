# Response.Result

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Placeholder for the response payload, whose actual shape depends on each endpoint’s concrete result type.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object Response.Result
```

#### Discussion

The `Response.Result` object represents the generic `result` field on the base [`Response`](response.md) type. Each endpoint returns a more specific type in its place, such as `Campaign` or `UserAccessResult`. See the endpoint’s own documentation for the concrete shape it returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/response/result-data.dictionary)*