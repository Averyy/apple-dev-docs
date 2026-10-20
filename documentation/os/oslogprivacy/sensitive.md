# sensitive

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The option to always redact interpolated values that contain sensitive information.

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
static var sensitive: OSLogPrivacy { get }
```

#### Discussion

This option behaves identically to the [`private`](./private.md) option. When it redacts a value, the system displays a generic string in place of the value. If you want to correlate log messages that contain the same value, use the [`sensitive(mask:)`](./sensitive%28mask%29.md) function to create the structure with the [`OSLogPrivacy.Mask.hash`](./mask/hash.md) mask.

## See Also

### Getting the Privacy Options
- [static var auto: OSLogPrivacy](./auto.md)
  The standard option to let the system determine whether to redact or display a value.
- [static var `private`: OSLogPrivacy](./private.md)
  The standard option to always redact the interpolated value.
- [static var `public`: OSLogPrivacy](./public.md)
  The standard option to always show the interpolated value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogprivacy/sensitive)*