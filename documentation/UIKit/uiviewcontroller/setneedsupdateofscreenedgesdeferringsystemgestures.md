# setNeedsUpdateOfScreenEdgesDeferringSystemGestures()

**Framework**: UIKit  
**Kind**: method

Notifies the system of changes to the screen edges that defer system gestures.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()
```

#### Discussion

Call this method whenever you modify the screen edges that defer system gestures, such as those that invoke Control Center, so the system can update accordingly. If the [`childForScreenEdgesDeferringSystemGestures`](uiviewcontroller/childforscreenedgesdeferringsystemgestures.md) property is `nil`, the system reads the edges from the current view controller’s [`preferredScreenEdgesDeferringSystemGestures`](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md) property; otherwise, it uses the same property on the referenced child view controller.

## See Also

- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md)
  The screen edges for which you want your gestures to take precedence over the system gestures.
- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](uiviewcontroller/childforscreenedgesdeferringsystemgestures.md)
  Returns the child view controller that should be queried to see if its gestures should take precedence.
- [var prefersHomeIndicatorAutoHidden: Bool](uiviewcontroller/prefershomeindicatorautohidden.md)
  A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [var childForHomeIndicatorAutoHidden: UIViewController?](uiviewcontroller/childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](uiviewcontroller/setneedsupdateofhomeindicatorautohidden.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures())*