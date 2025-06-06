# OSLogPrivacy.Mask.hash

**Framework**: os  
**Kind**: case

An option to replace a redacted value with a string that contains a hashed version of the original value.

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
case hash
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

#### Discussion

Use this option when you want to hide potentially sensitive data in log messages, but still want to know when two or more log messages contain the same hidden value. An [`OSLogPrivacy`](oslogprivacy.md) structure with this option generates a hash string for a redacted value. The system displays that hash string as part of the log message, making it possible for you to compare log messages with the same value.

## See Also

- [OSLogPrivacy.Mask.none](oslogprivacy/mask/none.md)
  An option to replace a redacted value with a generic string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy/mask/hash)*