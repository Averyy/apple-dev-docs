# OSLogPrivacy.Mask.none

**Framework**: os  
**Kind**: case  
**Role**: Case

An option to replace a redacted value with a generic string.

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
case none
```

## Discussion

Use this option when you don’t want to correlate log messages with identical redacted values.

## See Also

### Privacy Mask Options
- [OSLogPrivacy.Mask.hash](./hash.md)
  An option to replace a redacted value with a string that contains a hashed version of the original value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy/mask/none)*