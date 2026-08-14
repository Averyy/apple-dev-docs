# UIScreen.OverscanCompensation

**Framework**: UIKit  
**Kind**: enum

Describes different techniques for compensating for pixel loss at the edge of the screen.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+

## Declaration

```swift
enum OverscanCompensation
```

## Topics

### Constants
- [UIScreen.OverscanCompensation.scale](uiscreen/overscancompensation-swift.enum/scale.md)
  The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreen.OverscanCompensation.insetBounds](uiscreen/overscancompensation-swift.enum/insetbounds.md)
  The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.
- [UIScreen.OverscanCompensation.none](uiscreen/overscancompensation-swift.enum/none.md)
  No scaling occurs. Use [`overscanCompensationInsets`](uiscreen/overscancompensationinsets.md) to get the insets required to avoid clipping.
- [static var insetApplicationFrame: UIScreen.OverscanCompensation](uiscreen/overscancompensation-swift.enum/insetapplicationframe.md)
  The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped.
### Initializers
- [init?(rawValue: Int)](uiscreen/overscancompensation-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var overscanCompensationInsets: UIEdgeInsets](uiscreen/overscancompensationinsets.md)
  The edge inset values needed to avoid clipping the rectangle.
- [var overscanCompensation: UIScreen.OverscanCompensation](uiscreen/overscancompensation-swift.property.md)
  For an external screen, this property sets the desired technique to compensate for overscan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum)*