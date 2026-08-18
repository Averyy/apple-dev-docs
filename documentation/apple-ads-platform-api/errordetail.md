# ErrorDetail

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Field-level or request-level detail for a specific part of a failed API request.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ErrorDetail
```

#### Discussion

`ErrorDetail` provides field-level or request-level granularity for a specific part of a failed request. Each entry in the `Error.details` array is one `ErrorDetail`.

##### Example

```json
{
  "code": "FIELD_REQUIRED",
  "message": "campaign.name is required and was not provided for AwayFinder campaign creation."
}
```

## Properties

- `code` (string) *(required)*: A machine-readable code identifying the specific violation, such as `FIELD_REQUIRED` for a missing required field or `INVALID_VALUE` for a field that failed validation.
- `message` (string): A human-readable description of this specific violation, such as which field was missing or invalid and why.

## See Also

- [object Error](error.md)
  The standard error envelope that the API returns when a request fails.
- [object ErrorResponse](errorresponse.md)
  Certain endpoints return this envelope, which wraps an `Error` object, when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/errordetail)*