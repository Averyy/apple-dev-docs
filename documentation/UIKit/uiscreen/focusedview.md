# focusedView

**Framework**: UIKit  
**Kind**: property

The view that is currently focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
weak var focusedView: UIView? { get }
```

#### Discussion

When a view has focus, this property contains that view. When the focus is on an item that is not a view, the view in this property is the one that contains the item. This property is `nil` when nothing is currently focused on the screen.

## See Also

- [class var main: UIScreen](uiscreen/main.md)
  Returns the screen object representing the device’s screen.
- [class var screens: [UIScreen]](uiscreen/screens.md)
  Returns an array containing all of the screens attached to the device.
- [var applicationFrame: CGRect](uiscreen/applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedItem: (any UIFocusItem)?](uiscreen/focuseditem.md)
  The item that is currently focused.
- [var supportsFocus: Bool](uiscreen/supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/focusedview)*