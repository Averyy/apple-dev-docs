# UIScreen.ReferenceDisplayModeStatus

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### Statuses
- [UIScreen.ReferenceDisplayModeStatus.notSupported](uiscreen/referencedisplaymodestatus-swift.enum/notsupported.md)
  A status that indicates the screen doesn’t provide a reference display mode.
- [UIScreen.ReferenceDisplayModeStatus.notEnabled](uiscreen/referencedisplaymodestatus-swift.enum/notenabled.md)
  A status that indicates the screen provides a reference display mode but it’s in a disabled state.
- [UIScreen.ReferenceDisplayModeStatus.limited](uiscreen/referencedisplaymodestatus-swift.enum/limited.md)
  A status that indicates the screen’s in a limited reference display mode.
- [UIScreen.ReferenceDisplayModeStatus.enabled](uiscreen/referencedisplaymodestatus-swift.enum/enabled.md)
  A status that indicates the screen’s in an accurate reference display mode.
### Initializers
- [init?(rawValue: Int)](uiscreen/referencedisplaymodestatus-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var referenceDisplayModeStatus: UIScreen.ReferenceDisplayModeStatus](uiscreen/referencedisplaymodestatus-swift.property.md)
  The status of the screen’s reference display mode.
- [var currentEDRHeadroom: CGFloat](uiscreen/currentedrheadroom.md)
  The screen’s current headroom when displaying extended dynamic range content.
- [var potentialEDRHeadroom: CGFloat](uiscreen/potentialedrheadroom.md)
  The screen’s maximum headroom when displaying extended dynamic range content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/referencedisplaymodestatus-swift.enum)*