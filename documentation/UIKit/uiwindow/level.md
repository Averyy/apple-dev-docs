# UIWindow.Level

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The positioning of windows relative to each other.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct Level
```

```c
typedef CGFloat UIWindowLevel;
```

#### Overview

The stacking of levels takes precedence over the stacking of windows within each level. That is, even the bottom window in a level obscures the top window of the next level down. Levels are listed in order from lowest to highest.

## Topics

### Window levels
- [static let normal: UIWindow.Level](./level/normal.md)
  The default level.
- [static let statusBar: UIWindow.Level](./level/statusbar.md)
  The level for a status window.
- [static let alert: UIWindow.Level](./level/alert.md)
  The level for an alert view.
### Initializers
- [init(CGFloat)](./level/init%28_%29.md)
  Creates a window level structure.
- [init(rawValue: CGFloat)](./level/init%28rawvalue%29.md)
  Creates a window level structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the window
- [var rootViewController: UIViewController?](./rootviewcontroller.md)
  The root view controller for the window.
- [var windowLevel: UIWindow.Level](./windowlevel.md)
  The position of the window in the z-axis.
- [var canResizeToFitContent: Bool](./canresizetofitcontent.md)
  A Boolean value that indicates whether the window’s constraint-based content determines its size.
- [var screen: UIScreen](./screen.md)
  The screen to display the window on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/level)*