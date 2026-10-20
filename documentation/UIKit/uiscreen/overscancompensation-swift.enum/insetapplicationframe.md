# insetApplicationFrame

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The application frame is reduced in size to compensate for overscan. Content drawn outside the application frame may be clipped.

**Availability**:
- iOS 5.0+ - Deprecated in 9.0 (renamed: UIScreen.OverscanCompensation.none)
- iPadOS 5.0+ - Deprecated in 9.0 (renamed: UIScreen.OverscanCompensation.none)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: UIScreen.OverscanCompensation.none)
- tvOS - Deprecated in 9.0 (renamed: UIScreen.OverscanCompensation.none)

## Declaration

```swift
static var insetApplicationFrame: UIScreen.OverscanCompensation { get }
```

```c
UIScreenOverscanCompensationInsetApplicationFrame
```

## See Also

### Constants
- [UIScreen.OverscanCompensation.scale](./scale.md)
  The final composited framebuffer for the screen is scaled so that all pixels lie in the area visible on the screen.
- [UIScreen.OverscanCompensation.insetBounds](./insetbounds.md)
  The screen bounds are reduced in size so that all pixels in the framebuffer are visible on the screen.
- [UIScreen.OverscanCompensation.none](./none.md)
  No scaling occurs. Use [`overscanCompensationInsets`](../overscancompensationinsets.md) to get the insets required to avoid clipping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/overscancompensation-swift.enum/insetapplicationframe)*