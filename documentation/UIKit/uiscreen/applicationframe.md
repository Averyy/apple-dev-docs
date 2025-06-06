# applicationFrame

**Framework**: UIKit  
**Kind**: property

The frame rectangle for the app window, measured in points.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var applicationFrame: CGRect { get }
```

#### Discussion

This property contains the bounds rectangle used by the app window, which may be different than the screen bounds themselves. This rectangle is specified in the current coordinate space, which takes into account any interface rotations in effect for the device. Therefore, the value of this property may change when the device rotates between portrait and landscape orientations.

## See Also

- [class var main: UIScreen](uiscreen/main.md)
  Returns the screen object representing the device’s screen.
- [class var screens: [UIScreen]](uiscreen/screens.md)
  Returns an array containing all of the screens attached to the device.
- [var focusedItem: (any UIFocusItem)?](uiscreen/focuseditem.md)
  The item that is currently focused.
- [var focusedView: UIView?](uiscreen/focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](uiscreen/supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/applicationframe)*