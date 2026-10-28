# childForScreenEdgesDeferringSystemGestures

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the child view controller that should be queried to see if its gestures should take precedence.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var childForScreenEdgesDeferringSystemGestures: UIViewController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIViewController * childViewControllerForScreenEdgesDeferringSystemGestures;
```

## Mentions

- [Creating a custom container view controller](../creating-a-custom-container-view-controller.md)

## Discussion

When implementing a container view controller, override this method if one of your child view controllers defines screen-edge gestures that should take precedence over the system gestures. UIKit then uses the [`preferredScreenEdgesDeferringSystemGestures`](./preferredscreenedgesdeferringsystemgestures.md) property of the returned child view controller to determine which screen edges have competing gesture recognizers.

## See Also

### Coordinating with system gestures
- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](./preferredscreenedgesdeferringsystemgestures.md)
  The screen edges for which you want your gestures to take precedence over the system gestures.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](./setneedsupdateofscreenedgesdeferringsystemgestures%28%29.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var prefersHomeIndicatorAutoHidden: Bool](./prefershomeindicatorautohidden.md)
  A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [var childForHomeIndicatorAutoHidden: UIViewController?](./childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](./setneedsupdateofhomeindicatorautohidden%28%29.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childforscreenedgesdeferringsystemgestures)*