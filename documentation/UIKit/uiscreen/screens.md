# screens

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Returns an array containing all of the screens attached to the device.

**Availability**:
- iOS 3.2+ - Deprecated in 16.0
- iPadOS 3.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- tvOS - Deprecated in 16.0

> **Deprecated**: Use [`openSessions`](../uiapplication/opensessions.md) on the shared app object to find scenes for other screens.

## Declaration

```swift
class var screens: [UIScreen] { get }
```

```objc
@property (class, nonatomic, readonly) NSArray<UIScreen *> * screens;
```

## Return Value

An array of `UIScreen` objects.

## Discussion

The returned array includes the main screen plus any additional screens connected to the device. The main screen is always at index `0`.

Not all devices support external displays. iPhone and iPod touch devices with Retina displays and iPads support external displays. Older devices, such as the iPhone 3GS, don’t support external displays.

## See Also

### Deprecated properties
- [class var main: UIScreen](./main.md)
  Returns the screen object representing the device’s screen.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/screens)*