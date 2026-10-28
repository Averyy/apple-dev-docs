# applicationFrame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The frame rectangle for the app window, measured in points.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var applicationFrame: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect applicationFrame;
```

## Discussion

This property contains the bounds rectangle used by the app window, which may be different than the screen bounds themselves. This rectangle is specified in the current coordinate space, which takes into account any interface rotations in effect for the device. Therefore, the value of this property may change when the device rotates between portrait and landscape orientations.

## See Also

### Deprecated properties
- [class var main: UIScreen](./main.md)
  Returns the screen object representing the device’s screen.
- [class var screens: [UIScreen]](./screens.md)
  Returns an array containing all of the screens attached to the device.
- [var focusedItem: (any UIFocusItem)?](./focuseditem.md)
  The item that is currently focused.
- [var focusedView: UIView?](./focusedview.md)
  The view that is currently focused.
- [var supportsFocus: Bool](./supportsfocus.md)
  A Boolean value that indicates whether the screen supports focus-based inputs.
- [var isCaptured: Bool](./iscaptured.md)
  A Boolean value that indicates whether the system is actively cloning the screen to another destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/applicationframe)*