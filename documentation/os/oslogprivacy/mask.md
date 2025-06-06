# OSLogPrivacy.Mask

**Framework**: os  
**Kind**: enum

A mask that establishes how the system displays a redacted value in a log message.

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
enum Mask
```

## Topics

### Privacy Mask Options
- [OSLogPrivacy.Mask.hash](oslogprivacy/mask/hash.md)
  An option to replace a redacted value with a string that contains a hashed version of the original value.
- [OSLogPrivacy.Mask.none](oslogprivacy/mask/none.md)
  An option to replace a redacted value with a generic string.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [static func auto(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](oslogprivacy/auto(mask:).md)
  Returns a privacy structure that determines whether to redact or show values according to their type, and customizes the display of redacted values.
- [static func `private`(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](oslogprivacy/private(mask:).md)
  Returns a privacy structure that marks an interpolated value as private, and customizes the display of redacted values.
- [static func sensitive(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](oslogprivacy/sensitive(mask:).md)
  Returns a privacy structure that marks an interpolated value as sensitive, and customizes the display of redacted values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy/mask)*