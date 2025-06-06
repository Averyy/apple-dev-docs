# screen

**Framework**: UIKit  
**Kind**: property

The screen to display the window on.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var screen: UIScreen { get set }
```

#### Discussion

By default, UIKit sets this property to the primary device screen. If additional screens are attached to the device, you can assign a different screen object to display the window on that screen. A window is always displayed on only one screen.

Moving windows from screen to screen is a relatively expensive operation and isn’t optimal in performance-sensitive code. Instead, change the screen before displaying the window the first time. Changing the screen of a window that hasn’t been ordered onto the screen has no significant additional cost.

## See Also

- [var rootViewController: UIViewController?](uiwindow/rootviewcontroller.md)
  The root view controller for the window.
- [var windowLevel: UIWindow.Level](uiwindow/windowlevel.md)
  The position of the window in the z-axis.
- [UIWindow.Level](uiwindow/level.md)
  The positioning of windows relative to each other.
- [var canResizeToFitContent: Bool](uiwindow/canresizetofitcontent.md)
  A Boolean value that indicates whether the window’s constraint-based content determines its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/screen)*