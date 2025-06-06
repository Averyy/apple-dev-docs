# focusedItem

**Framework**: UIKit  
**Kind**: property

The item that is currently focused.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+

## Declaration

```swift
@MainActor
weak var focusedItem: (any UIFocusItem)? { get }
```

#### Discussion

If this item is not a view, the [`focusedView`](uiscreen/focusedview.md) property is set to the view that contains the item.

## See Also

- [class var main: UIScreen](uiscreen/main.md)
  Returns the screen object representing the device’s screen.
- [class var screens: [UIScreen]](uiscreen/screens.md)
  Returns an array containing all of the screens attached to the device.
- [var applicationFrame: CGRect](uiscreen/applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedView: UIView?](uiscreen/focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](uiscreen/supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/focuseditem)*