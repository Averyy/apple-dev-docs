# auto(mask:)

**Framework**: os  
**Kind**: method

Returns a privacy structure that determines whether to redact or show values according to their type, and customizes the display of redacted values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func auto(mask: OSLogPrivacy.Mask) -> OSLogPrivacy
```

#### Return Value

A privacy object that applies the default redaction rules.

## Parameters

- `mask`: A mask that determines whether the system replaces a redacted value with a generic string or a string from a hash of the redacted value.

## See Also

- [static func `private`(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](oslogprivacy/private(mask:).md)
  Returns a privacy structure that marks an interpolated value as private, and customizes the display of redacted values.
- [static func sensitive(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](oslogprivacy/sensitive(mask:).md)
  Returns a privacy structure that marks an interpolated value as sensitive, and customizes the display of redacted values.
- [OSLogPrivacy.Mask](oslogprivacy/mask.md)
  A mask that establishes how the system displays a redacted value in a log message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy/auto(mask:))*