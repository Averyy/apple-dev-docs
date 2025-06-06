# containerView

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The view that acts as the superview for the views involved in the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var containerView: UIView { get }
```

#### Return Value

The view that contains both views involved in the transition.

#### Discussion

The container view acts as the superview of all other views (including those of the presenting and presented view controllers) during the animation sequence. UIKit sets this view for you and automatically adds the view of the presenting view controller to it. The animator object is responsible for adding the view of the presented view controller, and the animator object or presentation controller must use this view as the container for all other views involved in the transition.

## See Also

- [func viewController(forKey: UITransitionContextViewControllerKey) -> UIViewController?](uiviewcontrollercontexttransitioning/viewcontroller(forkey:).md)
  Returns a view controller involved in the transition.
- [func view(forKey: UITransitionContextViewKey) -> UIView?](uiviewcontrollercontexttransitioning/view(forkey:).md)
  Returns the specified view involved in the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/containerview)*