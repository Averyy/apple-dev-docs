# UIScreen.OverscanCompensation.none

**Framework**: UIKit  
**Kind**: case

No scaling occurs. Use [`overscanCompensationInsets`](uiscreen/overscancompensationinsets.md) to get the insets required to avoid clipping.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
case none
```

## See Also

- [UIScreen.OverscanCompensation.scale](uiscreen/overscancompensation-swift.enum/scale.md)
  The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreen.OverscanCompensation.insetBounds](uiscreen/overscancompensation-swift.enum/insetbounds.md)
  The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.
- [static var insetApplicationFrame: UIScreen.OverscanCompensation](uiscreen/overscancompensation-swift.enum/insetapplicationframe.md)
  The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum/none)*