# childForScreenEdgesDeferringSystemGestures

**Framework**: UIKit  
**Kind**: property

Returns the child view controller that should be queried to see if its gestures should take precedence.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var childForScreenEdgesDeferringSystemGestures: UIViewController? { get }
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)

#### Discussion

When implementing a container view controller, override this method if one of your child view controllers defines screen-edge gestures that should take precedence over the system gestures. UIKit then uses the [`preferredScreenEdgesDeferringSystemGestures`](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md) property of the returned child view controller to determine which screen edges have competing gesture recognizers.

## See Also

- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md)
  The screen edges for which you want your gestures to take precedence over the system gestures.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var prefersHomeIndicatorAutoHidden: Bool](uiviewcontroller/prefershomeindicatorautohidden.md)
  A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [var childForHomeIndicatorAutoHidden: UIViewController?](uiviewcontroller/childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](uiviewcontroller/setneedsupdateofhomeindicatorautohidden.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childforscreenedgesdeferringsystemgestures)*