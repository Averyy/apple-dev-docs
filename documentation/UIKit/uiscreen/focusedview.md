# focusedView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view that is currently focused.

**Availability**:
- iOS 9.0+ - Deprecated in 15.0
- iPadOS 9.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 15.0

> **Deprecated**: Use [`focusedItem`](../uifocussystem/focuseditem.md) in [`focusSystem`](../uiwindowscene/focussystem.md) instead.

## Declaration

```swift
weak var focusedView: UIView? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) UIView * focusedView;
```

#### Discussion

When a view has focus, this property contains that view. When the focus is on an item that is not a view, the view in this property is the one that contains the item. This property is `nil` when nothing is currently focused on the screen.

## See Also

### Deprecated properties
- [class var main: UIScreen](./main.md)
  Returns the screen object representing the device’s screen.
- [class var screens: [UIScreen]](./screens.md)
  Returns an array containing all of the screens attached to the device.
- [var applicationFrame: CGRect](./applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedItem: (any UIFocusItem)?](./focuseditem.md)
  The item that is currently focused.
- [var supportsFocus: Bool](./supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.
- [var isCaptured: Bool](./iscaptured.md)
  A Boolean value that indicates whether the system is actively cloning the screen to another destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/focusedview)*