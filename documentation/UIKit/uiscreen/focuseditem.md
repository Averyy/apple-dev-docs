# focusedItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The item that is currently focused.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS 10.0+ - Deprecated in 15.0

> **Deprecated**: Use [`focusedItem`](../uifocussystem/focuseditem.md) in [`focusSystem`](../uiwindowscene/focussystem.md) instead.

## Declaration

```swift
weak var focusedItem: (any UIFocusItem)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UIFocusItem> focusedItem;
```

#### Discussion

If this item is not a view, the [`focusedView`](./focusedview.md) property is set to the view that contains the item.

## See Also

### Deprecated properties
- [class var main: UIScreen](./main.md)
  Returns the screen object representing the device’s screen.
- [class var screens: [UIScreen]](./screens.md)
  Returns an array containing all of the screens attached to the device.
- [var applicationFrame: CGRect](./applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedView: UIView?](./focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](./supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.
- [var isCaptured: Bool](./iscaptured.md)
  A Boolean value that indicates whether the system is actively cloning the screen to another destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/focuseditem)*