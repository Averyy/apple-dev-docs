# prefersHomeIndicatorAutoHidden

**Framework**: UIKit  
**Kind**: property

A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var prefersHomeIndicatorAutoHidden: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if your view controller lets the system determine when to hide the indicator, or [`false`](https://developer.apple.com/documentation/swift/false) if you want the indicator to show at all times. The default implementation of this method returns [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Override this method to signal your preference for displaying the visual indicator. The system takes your preference into account, but returning [`true`](https://developer.apple.com/documentation/swift/true) is no guarantee that the indicator will be hidden.

For information on allowing app-defined gestures to take precedence over system gestures for certain screen edges, see [`preferredScreenEdgesDeferringSystemGestures`](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md).

## See Also

- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](uiviewcontroller/preferredscreenedgesdeferringsystemgestures.md)
  The screen edges for which you want your gestures to take precedence over the system gestures.
- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](uiviewcontroller/childforscreenedgesdeferringsystemgestures.md)
  Returns the child view controller that should be queried to see if its gestures should take precedence.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](uiviewcontroller/setneedsupdateofscreenedgesdeferringsystemgestures.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var childForHomeIndicatorAutoHidden: UIViewController?](uiviewcontroller/childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](uiviewcontroller/setneedsupdateofhomeindicatorautohidden.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/prefershomeindicatorautohidden)*