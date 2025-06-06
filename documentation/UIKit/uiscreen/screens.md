# screens

**Framework**: UIKit  
**Kind**: property

Returns an array containing all of the screens attached to the device.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
class var screens: [UIScreen] { get }
```

#### Return Value

An array of `UIScreen` objects.

#### Discussion

The returned array includes the main screen plus any additional screens connected to the device. The main screen is always at index `0`.

Not all devices support external displays. iPhone and iPod touch devices with Retina displays and iPads support external displays. Older devices, such as the iPhone 3GS, don’t support external displays.

## See Also

- [class var main: UIScreen](uiscreen/main.md)
  Returns the screen object representing the device’s screen.
- [var applicationFrame: CGRect](uiscreen/applicationframe.md)
  The frame rectangle for the app window, measured in points.
- [var focusedItem: (any UIFocusItem)?](uiscreen/focuseditem.md)
  The item that is currently focused.
- [var focusedView: UIView?](uiscreen/focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](uiscreen/supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/screens)*