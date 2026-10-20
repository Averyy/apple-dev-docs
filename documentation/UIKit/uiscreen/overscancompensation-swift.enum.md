# UIScreen.OverscanCompensation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Describes different techniques for compensating for pixel loss at the edge of the screen.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS

## Declaration

```swift
enum OverscanCompensation
```

```c
enum UIScreenOverscanCompensation : NSInteger;
```

## Topics

### Constants
- [UIScreen.OverscanCompensation.scale](./overscancompensation-swift.enum/scale.md)
  The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreen.OverscanCompensation.insetBounds](./overscancompensation-swift.enum/insetbounds.md)
  The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.
- [UIScreen.OverscanCompensation.none](./overscancompensation-swift.enum/none.md)
  No scaling occurs. Use [`overscanCompensationInsets`](./overscancompensationinsets.md) to get the insets required to avoid clipping.
- [static var insetApplicationFrame: UIScreen.OverscanCompensation](./overscancompensation-swift.enum/insetapplicationframe.md)
  The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped.
### Initializers
- [init?(rawValue: Int)](./overscancompensation-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing overscan compensation
- [var overscanCompensationInsets: UIEdgeInsets](./overscancompensationinsets.md)
  The edge inset values needed to avoid clipping the rectangle.
- [var overscanCompensation: UIScreen.OverscanCompensation](./overscancompensation-swift.property.md)
  For an external screen, this property sets the desired technique to compensate for overscan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum)*