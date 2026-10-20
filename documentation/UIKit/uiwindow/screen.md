# screen

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The screen to display the window on.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS

> **Deprecated**: Use [`windowScene`](./windowscene.md) instead.

## Declaration

```swift
var screen: UIScreen { get set }
```

```objc
@property (nonatomic, strong) UIScreen * screen;
```

#### Discussion

By default, UIKit sets this property to the primary device screen. If additional screens are attached to the device, you can assign a different screen object to display the window on that screen. A window is always displayed on only one screen.

Moving windows from screen to screen is a relatively expensive operation and isn’t optimal in performance-sensitive code. Instead, change the screen before displaying the window the first time. Changing the screen of a window that hasn’t been ordered onto the screen has no significant additional cost.

## See Also

### Configuring the window
- [var rootViewController: UIViewController?](./rootviewcontroller.md)
  The root view controller for the window.
- [var windowLevel: UIWindow.Level](./windowlevel.md)
  The position of the window in the z-axis.
- [UIWindow.Level](./level.md)
  The positioning of windows relative to each other.
- [var canResizeToFitContent: Bool](./canresizetofitcontent.md)
  A Boolean value that indicates whether the window’s constraint-based content determines its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/screen)*