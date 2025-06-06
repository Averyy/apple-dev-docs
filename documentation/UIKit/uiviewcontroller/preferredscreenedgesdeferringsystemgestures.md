# preferredScreenEdgesDeferringSystemGestures

**Framework**: UIKit  
**Kind**: property

The screen edges for which you want your gestures to take precedence over the system gestures.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredScreenEdgesDeferringSystemGestures: UIRectEdge { get }
```

#### Discussion

Normally, the screen-edge gestures defined by the system take precedence over any gesture recognizers that you define. The system uses its gestures to implement system-level behaviors, such as to display Control Center.

Whenever possible, you should allow the system gestures to take precedence. However, immersive apps can use this property to allow app-defined gestures to take precedence over the system gestures. You do that by overriding this property and returning the screen edges for which your gestures should take precedence.

If you change the edges preferred by your view controller, update the value of this property and call the [`setNeedsUpdateOfScreenEdgesDeferringSystemGestures()`](uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures().md) method to notify the system that the edges have changed.

For information on showing and hiding the visual indicator for returning to the Home Screen, see [`prefersHomeIndicatorAutoHidden`](uiviewcontroller/prefershomeindicatorautohidden.md).

## See Also

- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](uiviewcontroller/childforscreenedgesdeferringsystemgestures.md)
  Returns the child view controller that should be queried to see if its gestures should take precedence.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var prefersHomeIndicatorAutoHidden: Bool](uiviewcontroller/prefershomeindicatorautohidden.md)
  A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [var childForHomeIndicatorAutoHidden: UIViewController?](uiviewcontroller/childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](uiviewcontroller/setneedsupdateofhomeindicatorautohidden.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredscreenedgesdeferringsystemgestures)*