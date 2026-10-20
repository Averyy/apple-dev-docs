# private

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The standard option to always redact the interpolated value.

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
static var `private`: OSLogPrivacy { get }
```

## Mentions

- [Generating Log Messages from Your Code](../generating-log-messages-from-your-code.md)

#### Discussion

When it redacts a value, the system displays a generic string in place of the value. If you want to correlate log messages that contain the same value, use the [`private(mask:)`](./private%28mask%29.md) function to create a structure with the [`OSLogPrivacy.Mask.hash`](./mask/hash.md) mask.

## See Also

### Getting the Privacy Options
- [static var auto: OSLogPrivacy](./auto.md)
  The standard option to let the system determine whether to redact or display a value.
- [static var `public`: OSLogPrivacy](./public.md)
  The standard option to always show the interpolated value.
- [static var sensitive: OSLogPrivacy](./sensitive.md)
  The option to always redact interpolated values that contain sensitive information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy/private)*