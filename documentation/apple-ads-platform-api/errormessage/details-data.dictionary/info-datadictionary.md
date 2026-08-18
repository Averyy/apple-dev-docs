# ErrorMessage.Details.Info

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

An object (string-to-string map) with additional structured context for a specific validation failure.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ErrorMessage.Details.Info
```

#### Discussion

Each key names a piece of context specific to the failure, such as `field`, not a fixed field name. `info` is a free-form map rather than an object with named properties, so the reference page labels this key `Any Key`. For example, when a request fails because it omits the required `eventTime` filter, the top-level [`ErrorMessage`](errormessage.md) example shows a `details` entry with `info: { "field": "eventTime" }`, naming the missing field.

## Properties

- `Any Key` (string)


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/errormessage/details-data.dictionary/info-data.dictionary)*