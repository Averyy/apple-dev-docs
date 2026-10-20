# OSLogPrivacy.Mask

**Framework**: os  
**Kind**: enum  
**Role**: Enumeration

A mask that establishes how the system displays a redacted value in a log message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
enum Mask
```

## Topics

### Privacy Mask Options
- [OSLogPrivacy.Mask.hash](./mask/hash.md)
  An option to replace a redacted value with a string that contains a hashed version of the original value.
- [OSLogPrivacy.Mask.none](./mask/none.md)
  An option to replace a redacted value with a generic string.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Creating a Custom Privacy Mask
- [static func auto(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](./auto%28mask%29.md)
  Returns a privacy structure that determines whether to redact or show values according to their type, and customizes the display of redacted values.
- [static func `private`(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](./private%28mask%29.md)
  Returns a privacy structure that marks an interpolated value as private, and customizes the display of redacted values.
- [static func sensitive(mask: OSLogPrivacy.Mask) -> OSLogPrivacy](./sensitive%28mask%29.md)
  Returns a privacy structure that marks an interpolated value as sensitive, and customizes the display of redacted values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy/mask)*