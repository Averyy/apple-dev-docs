# childForHomeIndicatorAutoHidden

**Framework**: UIKit  
**Kind**: property

Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var childForHomeIndicatorAutoHidden: UIViewController? { get }
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)

#### Return Value

The child view controller to consult. The default implementation of this method returns `nil`.

#### Discussion

When implementing a container view controller, override this method if you want one your child view controllers to determine whether to display the visual indicator. If you do, the system calls the [`prefersHomeIndicatorAutoHidden`](uiviewcontroller/prefershomeindicatorautohidden.md) method of the returned view controller. If the method returns `nil`, the system calls the [`prefersHomeIndicatorAutoHidden`](uiviewcontroller/prefershomeindicatorautohidden.md) method of the current view controller.

## See Also

- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md)
  The screen edges for which you want your gestures to take precedence over the system gestures.
- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](uiviewcontroller/childforscreenedgesdeferringsystemgestures.md)
  Returns the child view controller that should be queried to see if its gestures should take precedence.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var prefersHomeIndicatorAutoHidden: Bool](uiviewcontroller/prefershomeindicatorautohidden.md)
  A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](uiviewcontroller/setneedsupdateofhomeindicatorautohidden.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childforhomeindicatorautohidden)*