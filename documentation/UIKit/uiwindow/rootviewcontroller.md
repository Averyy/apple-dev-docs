# rootViewController

**Framework**: UIKit  
**Kind**: property

The root view controller for the window.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var rootViewController: UIViewController? { get set }
```

## Mentions

- [Managing content in your app’s windows](managing-content-in-your-app-s-windows.md)

#### Discussion

The root view controller provides the content view of the window. Assigning a view controller to this property (either programmatically or using Interface Builder) installs the view controller’s view as the content view of the window. The new content view is configured to track the window size, changing as the window size changes. If the window has an existing view hierarchy, the old views are removed before the new ones are installed.

The default value of this property is `nil`.

## See Also

- [var windowLevel: UIWindow.Level](uiwindow/windowlevel.md)
  The position of the window in the z-axis.
- [UIWindow.Level](uiwindow/level.md)
  The positioning of windows relative to each other.
- [var canResizeToFitContent: Bool](uiwindow/canresizetofitcontent.md)
  A Boolean value that indicates whether the window’s constraint-based content determines its size.
- [var screen: UIScreen](uiwindow/screen.md)
  The screen to display the window on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/rootviewcontroller)*