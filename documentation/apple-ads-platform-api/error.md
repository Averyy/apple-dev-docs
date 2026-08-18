# Error

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The standard error envelope that the API returns when a request fails.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Error
```

#### Discussion

`Error` is the standard error envelope that the API returns when a request fails.

Change History endpoints use a separate, ChangeHistory-specific error object, [`ErrorMessage`](errormessage.md), whose `code` is a closed enum (`BAD_REQUEST`, `NOT_FOUND`, `NOT_AUTHED`) rather than the open string used here.

Check `details` when you need to pinpoint exactly which part of the request was invalid, for example, a specific field value that violated a constraint or a missing required parameter.

##### Example

```json
{
  "code": "INVALID_ARGUMENT",
  "message": "The request could not be processed because one or more fields failed validation.",
  "details": [
    {
      "code": "FIELD_REQUIRED",
      "message": "campaign.name is required and was not provided for AwayFinder campaign creation."
    }
  ]
}
```

## Properties

- `code` (string) *(required)*: The reason the API rejected the request (such as `INVALID_ARGUMENT` or `UNAUTHORIZED`).
- `message` (string): A human-readable error summary of what went wrong at the request level.
- `details` ([ErrorDetail]): An array of zero or more error details objects that describe specific field-level or request-level violations. See [`ErrorDetail`](errordetail.md).

## See Also

- [object ErrorDetail](errordetail.md)
  Field-level or request-level detail for a specific part of a failed API request.
- [object ErrorResponse](errorresponse.md)
  Certain endpoints return this envelope, which wraps an `Error` object, when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/error)*