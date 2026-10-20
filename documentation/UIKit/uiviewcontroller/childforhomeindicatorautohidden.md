# childForHomeIndicatorAutoHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var childForHomeIndicatorAutoHidden: UIViewController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIViewController * childViewControllerForHomeIndicatorAutoHidden;
```

## Mentions

- [Creating a custom container view controller](../creating-a-custom-container-view-controller.md)

#### Return Value

The child view controller to consult. The default implementation of this method returns `nil`.

#### Discussion

When implementing a container view controller, override this method if you want one your child view controllers to determine whether to display the visual indicator. If you do, the system calls the [`prefersHomeIndicatorAutoHidden`](./prefershomeindicatorautohidden.md) method of the returned view controller. If the method returns `nil`, the system calls the [`prefersHomeIndicatorAutoHidden`](./prefershomeindicatorautohidden.md) method of the current view controller.

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
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](./setneedsupdateofhomeindicatorautohidden%28%29.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childforhomeindicatorautohidden)*