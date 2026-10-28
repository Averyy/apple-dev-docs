# main

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Returns the screen object representing the device’s screen.

**Availability**:
- iOS 2.0+ - Deprecated in 26.0
- iPadOS 2.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0

> **Deprecated**: Use [`screen`](../uiwindowscene/screen.md) instead.

## Declaration

```swift
class var main: UIScreen { get }
```

```objc
@property (class, nonatomic, readonly) UIScreen * mainScreen;
```

## Return Value

The screen object for the device.

## Discussion

Apple discourages the use of this symbol. Use a [`UIScreen`](../uiscreen.md) instance found through context instead. For example, reference the screen that displays a view through the [`screen`](../uiwindowscene/screen.md) property on the window scene managing the window containing the view.

## See Also

### Deprecated properties
- [class var screens: [UIScreen]](./screens.md)
  Returns an array containing all of the screens attached to the device.
- [var applicationFrame: CGRect](./applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedItem: (any UIFocusItem)?](./focuseditem.md)
  The item that is currently focused.
- [var focusedView: UIView?](./focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](./supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.
- [var isCaptured: Bool](./iscaptured.md)
  A Boolean value that indicates whether the system is actively cloning the screen to another destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/main)*