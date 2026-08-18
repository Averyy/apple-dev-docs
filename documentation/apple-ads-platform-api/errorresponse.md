# ErrorResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Certain endpoints return this envelope, which wraps an `Error` object, when a request fails.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ErrorResponse
```

#### Discussion

`ErrorResponse` is a response envelope that wraps an `Error` object. Certain endpoints return it when a request fails, providing the full `Error` structure including `code`, `message`, and `details`.

A `429` status indicates the caller has exceeded its request quota. See [`Applying Rate Limits`](rate-limits.md) for the rate-limit headers and a sample backoff implementation to use before retrying.

##### Example

```json
{
  "error": {
    "code": "INVALID_ARGUMENT",
    "message": "The request could not be processed because of missing or invalid fields.",
    "details": [
      {
        "code": "MISSING_REQUIRED_FIELD",
        "message": "The field 'name' is required for campaign AwayFinder Summer Launch."
      }
    ]
  }
}
```

## Properties

- `error` (Error): The error object containing details about the failure. See [`Error`](error.md).

## See Also

- [object Error](error.md)
  The standard error envelope that the API returns when a request fails.
- [object ErrorDetail](errordetail.md)
  Field-level or request-level detail for a specific part of a failed API request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/errorresponse)*