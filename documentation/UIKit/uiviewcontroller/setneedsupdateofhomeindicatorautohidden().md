# setNeedsUpdateOfHomeIndicatorAutoHidden()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setNeedsUpdateOfHomeIndicatorAutoHidden()
```

```objc
- (void) setNeedsUpdateOfHomeIndicatorAutoHidden;
```

## Discussion

When you change the value returned by your view controller’s [`prefersHomeIndicatorAutoHidden`](./prefershomeindicatorautohidden.md) or [`childForHomeIndicatorAutoHidden`](./childforhomeindicatorautohidden.md) method, call this method to let UIKit know that it should call those methods again.

## See Also

### Coordinating with system gestures
- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](./preferredscreenedgesdeferringsystemgestures.md)
  The screen edges for which you want your gestures to take precedence over the system gestures.
- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](./childforscreenedgesdeferringsystemgestures.md)
  Returns the child view controller that should be queried to see if its gestures should take precedence.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](./setneedsupdateofscreenedgesdeferringsystemgestures%28%29.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var prefersHomeIndicatorAutoHidden: Bool](./prefershomeindicatorautohidden.md)
  A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [var childForHomeIndicatorAutoHidden: UIViewController?](./childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofhomeindicatorautohidden())*