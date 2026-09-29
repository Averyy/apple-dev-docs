# Info

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Additional context that supplements an error detail’s message, varying by endpoint and error type.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object Info
```

#### Discussion

`Info` supplements an [`ErrorDetail`](errordetail.md)’s `message` with structured context, such as the field name, the invalid value, or acceptable alternatives. Its shape depends on the endpoint and the specific error condition, so it carries no fixed set of properties.

## See Also

- [object Error](error.md)
  The standard error envelope that the API returns when a request fails.
- [object ErrorDetail](errordetail.md)
  Field-level or request-level detail for a specific part of a failed API request.
- [object ErrorResponse](errorresponse.md)
  Certain endpoints return this envelope, which wraps an `Error` object, when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/info)*