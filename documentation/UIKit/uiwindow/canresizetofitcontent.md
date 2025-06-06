# canResizeToFitContent

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the window’s constraint-based content determines its size.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canResizeToFitContent: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false), which causes the window to maintain a fixed size. Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) allows the system to perform constraints-based window sizing, which updates the window’s size to match the space needed by its content. Window-size changes occur only when the app runs on macOS.

## See Also

- [var rootViewController: UIViewController?](uiwindow/rootviewcontroller.md)
  The root view controller for the window.
- [var windowLevel: UIWindow.Level](uiwindow/windowlevel.md)
  The position of the window in the z-axis.
- [UIWindow.Level](uiwindow/level.md)
  The positioning of windows relative to each other.
- [var screen: UIScreen](uiwindow/screen.md)
  The screen to display the window on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/canresizetofitcontent)*