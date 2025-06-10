# UIWindow.Level

**Framework**: UIKit  
**Kind**: struct

The positioning of windows relative to each other.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct Level
```

#### Overview

The stacking of levels takes precedence over the stacking of windows within each level. That is, even the bottom window in a level obscures the top window of the next level down. Levels are listed in order from lowest to highest.

## Topics

### Window levels
- [static let normal: UIWindow.Level](uiwindow/level/normal.md)
  The default level.
- [static let statusBar: UIWindow.Level](uiwindow/level/statusbar.md)
  The level for a status window.
- [static let alert: UIWindow.Level](uiwindow/level/alert.md)
  The level for an alert view.
### Initializers
- [init(CGFloat)](uiwindow/level/init(_:).md)
  Creates a window level structure.
- [init(rawValue: CGFloat)](uiwindow/level/init(rawvalue:).md)
  Creates a window level structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var rootViewController: UIViewController?](uiwindow/rootviewcontroller.md)
  The root view controller for the window.
- [var windowLevel: UIWindow.Level](uiwindow/windowlevel.md)
  The position of the window in the z-axis.
- [var canResizeToFitContent: Bool](uiwindow/canresizetofitcontent.md)
  A Boolean value that indicates whether the window’s constraint-based content determines its size.
- [var screen: UIScreen](uiwindow/screen.md)
  The screen to display the window on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/level)*