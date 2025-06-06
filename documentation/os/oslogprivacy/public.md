# public

**Framework**: os  
**Kind**: property

The standard option to always show the interpolated value.

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
static var `public`: OSLogPrivacy { get }
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

## See Also

- [static var auto: OSLogPrivacy](oslogprivacy/auto.md)
  The standard option to let the system determine whether to redact or display a value.
- [static var `private`: OSLogPrivacy](oslogprivacy/private.md)
  The standard option to always redact the interpolated value.
- [static var sensitive: OSLogPrivacy](oslogprivacy/sensitive.md)
  The option to always redact interpolated values that contain sensitive information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy/public)*