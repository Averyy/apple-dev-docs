# prefersHomeIndicatorAutoHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var prefersHomeIndicatorAutoHidden: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL prefersHomeIndicatorAutoHidden;
```

## Return Value

[`true`](../../Swift/true.md) if your view controller lets the system determine when to hide the indicator, or [`false`](../../Swift/false.md) if you want the indicator to show at all times. The default implementation of this method returns [`false`](../../Swift/false.md).

## Discussion

Override this method to signal your preference for displaying the visual indicator. The system takes your preference into account, but returning [`true`](../../Swift/true.md) is no guarantee that the indicator will be hidden.

For information on allowing app-defined gestures to take precedence over system gestures for certain screen edges, see [`preferredScreenEdgesDeferringSystemGestures`](./preferredscreenedgesdeferringsystemgestures.md).

## See Also

### Coordinating with system gestures
- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](./preferredscreenedgesdeferringsystemgestures.md)
  The screen edges for which you want your gestures to take precedence over the system gestures.
- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](./childforscreenedgesdeferringsystemgestures.md)
  Returns the child view controller that should be queried to see if its gestures should take precedence.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](./setneedsupdateofscreenedgesdeferringsystemgestures%28%29.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var childForHomeIndicatorAutoHidden: UIViewController?](./childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](./setneedsupdateofhomeindicatorautohidden%28%29.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/prefershomeindicatorautohidden)*