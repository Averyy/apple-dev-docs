# UIScreen.OverscanCompensation.insetBounds

**Framework**: UIKit  
**Kind**: case

The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+

## Declaration

```swift
case insetBounds
```

## See Also

- [UIScreen.OverscanCompensation.scale](uiscreen/overscancompensation-swift.enum/scale.md)
  The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreen.OverscanCompensation.none](uiscreen/overscancompensation-swift.enum/none.md)
  No scaling occurs. Use [`overscanCompensationInsets`](uiscreen/overscancompensationinsets.md) to get the insets required to avoid clipping.
- [static var insetApplicationFrame: UIScreen.OverscanCompensation](uiscreen/overscancompensation-swift.enum/insetapplicationframe.md)
  The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum/insetbounds)*