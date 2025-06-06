# windowLevel

**Framework**: UIKit  
**Kind**: property

The position of the window in the z-axis.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var windowLevel: UIWindow.Level { get set }
```

#### Discussion

Window levels provide a relative grouping of windows along the z-axis. All windows assigned to the same window level appear in front of (or behind) all windows assigned to a different window level. The ordering of windows within a given window level is not guaranteed.

The default value of this property is [`normal`](uiwindow/level/normal.md). For a list of other possible window levels, see [`UIWindow.Level`](uiwindow/level.md).

## See Also

- [var rootViewController: UIViewController?](uiwindow/rootviewcontroller.md)
  The root view controller for the window.
- [UIWindow.Level](uiwindow/level.md)
  The positioning of windows relative to each other.
- [var canResizeToFitContent: Bool](uiwindow/canresizetofitcontent.md)
  A Boolean value that indicates whether the window’s constraint-based content determines its size.
- [var screen: UIScreen](uiwindow/screen.md)
  The screen to display the window on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/windowlevel)*