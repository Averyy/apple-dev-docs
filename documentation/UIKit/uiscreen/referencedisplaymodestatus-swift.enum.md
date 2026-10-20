# UIScreen.ReferenceDisplayModeStatus

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Describes a screen’s reference display mode status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+

## Declaration

```swift
enum ReferenceDisplayModeStatus
```

```c
enum UIScreenReferenceDisplayModeStatus : NSInteger;
```

## Topics

### Statuses
- [UIScreen.ReferenceDisplayModeStatus.notSupported](./referencedisplaymodestatus-swift.enum/notsupported.md)
  A status that indicates the screen doesn’t provide a reference display mode.
- [UIScreen.ReferenceDisplayModeStatus.notEnabled](./referencedisplaymodestatus-swift.enum/notenabled.md)
  A status that indicates the screen provides a reference display mode but it’s in a disabled state.
- [UIScreen.ReferenceDisplayModeStatus.limited](./referencedisplaymodestatus-swift.enum/limited.md)
  A status that indicates the screen’s in a limited reference display mode.
- [UIScreen.ReferenceDisplayModeStatus.enabled](./referencedisplaymodestatus-swift.enum/enabled.md)
  A status that indicates the screen’s in an accurate reference display mode.
### Initializers
- [init?(rawValue: Int)](./referencedisplaymodestatus-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the reference display mode status
- [var referenceDisplayModeStatus: UIScreen.ReferenceDisplayModeStatus](./referencedisplaymodestatus-swift.property.md)
  The status of the screen’s reference display mode.
- [var currentEDRHeadroom: CGFloat](./currentedrheadroom.md)
  The screen’s current headroom when displaying extended dynamic range content.
- [var potentialEDRHeadroom: CGFloat](./potentialedrheadroom.md)
  The screen’s maximum headroom when displaying extended dynamic range content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum)*