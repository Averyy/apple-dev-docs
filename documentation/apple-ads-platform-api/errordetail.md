# ErrorDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Field-level or request-level detail for a specific part of a failed API request.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object ErrorDetail
```

#### Discussion

The `ErrorDetail` provides field-level or request-level granularity for a specific part of a failed request. Each entry in the `Error.details` array is one `ErrorDetail`.

##### Example

```json
{
  "code": "FIELD_REQUIRED",
  "message": "campaign.name is required and was not provided for AwayFinder campaign creation.",
  "info": {
    "field": "campaign.name"
  }
}
```

## Properties

- `code` (string) *(required)*: A machine-readable code identifying the specific violation, such as `FIELD_REQUIRED` for a missing required field or `INVALID_VALUE` for a field that failed validation.
- `message` (string): A human-readable description of this specific violation, such as which field was missing or invalid and why.
- `info` (Info): Additional context that supplements `message`, such as the field name, the invalid value, or acceptable alternatives. Content varies by endpoint and error type. See [`Info`](info.md).

## See Also

- [object Error](error.md)
  The standard error envelope that the API returns when a request fails.
- [object ErrorResponse](errorresponse.md)
  Certain endpoints return this envelope, which wraps an `Error` object, when a request fails.
- [object Info](info.md)
  Additional context that supplements an error detail’s message, varying by endpoint and error type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/errordetail)*