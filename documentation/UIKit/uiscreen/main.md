# main

**Framework**: UIKit  
**Kind**: property

Returns the screen object representing the device’s screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
class var main: UIScreen { get }
```

#### Return Value

The screen object for the device.

#### Discussion

Apple discourages the use of this symbol. Use a [`UIScreen`](uiscreen.md) instance found through context instead. For example, reference the screen that displays a view through the [`screen`](uiwindowscene/screen.md) property on the window scene managing the window containing the view.

## See Also

- [class var screens: [UIScreen]](uiscreen/screens.md)
  Returns an array containing all of the screens attached to the device.
- [var applicationFrame: CGRect](uiscreen/applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedItem: (any UIFocusItem)?](uiscreen/focuseditem.md)
  The item that is currently focused.
- [var focusedView: UIView?](uiscreen/focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](uiscreen/supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/main)*