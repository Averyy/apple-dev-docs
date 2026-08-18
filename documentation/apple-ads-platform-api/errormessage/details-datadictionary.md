# ErrorMessage.Details

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single error detail entry describing one part of a failed change history request.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ErrorMessage.Details
```

#### Discussion

Each entry in `ErrorMessage`’s `details` array narrows down which part of the request caused the failure. Use these entries, together with the top-level `message`, for diagnostic logging or user-facing error displays. Use the top-level `code` on [`ErrorMessage`](errormessage.md) for programmatic error handling.

##### Example

```json
{
  "code": "MISSING_FIELD",
  "message": "eventTime must be provided.",
  "info": {
    "field": "eventTime"
  }
}
```

## Topics

### Dictionaries
- [object ErrorMessage.Details.Info](errormessage/details-data.dictionary/info-data.dictionary.md)
  An object (string-to-string map) with additional structured context for a specific validation failure.

## Properties

- `code` (string): A machine-readable code identifying the specific validation failure. Read-only.
- `message` (string): A human-readable description of this detail entry. Read-only.
- `info` (ErrorMessage.Details.Info): Additional structured context for this failure. See [`ErrorMessage.Details.Info`](errormessage/details-data.dictionary/info-data.dictionary.md). Read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/errormessage/details-data.dictionary)*