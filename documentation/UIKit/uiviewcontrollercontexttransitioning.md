# UIViewControllerContextTransitioning

**Framework**: UIKit  
**Kind**: protocol

A set of methods that provide contextual information for transition animations between view controllers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIViewControllerContextTransitioning : NSObjectProtocol
```

#### Overview

Don’t adopt this protocol in your own classes, nor should you directly create objects that adopt this protocol. During a transition, the animator objects involved in that transition receive a fully configured context object from UIKit. Custom animator objects — objects that adopt the [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) or [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md) protocol — should simply retrieve the information they need from the provided object.

A context object encapsulates information about the views and view controllers involved in the transition. It also contains details about the how to execute the transition. For interactive transitions, the interactive animator object uses the methods of this protocol to report the animation’s progress. When the animation starts, the interactive animator object must save a pointer to the context object. Based on user interactions, the animator object then calls the [`updateInteractiveTransition(_:)`](uiviewcontrollercontexttransitioning/updateinteractivetransition(_:).md), [`finishInteractiveTransition()`](uiviewcontrollercontexttransitioning/finishinteractivetransition().md), or [`cancelInteractiveTransition()`](uiviewcontrollercontexttransitioning/cancelinteractivetransition().md) methods to report the progress toward completing the animation. Those methods send that information to UIKit so that it can drive the timing of the animations.

> ❗ **Important**:  When defining custom animator objects, always check the value returned by the [`isAnimated`](uiviewcontrollercontexttransitioning/isanimated.md) method to determine whether you should create animations at all. And when you do create transition animations, always call the [`completeTransition(_:)`](uiviewcontrollercontexttransitioning/completetransition(_:).md) method from an appropriate completion block to let UIKit know when all of your animations have finished.

## Topics

### Accessing the transition objects
- [var containerView: UIView](uiviewcontrollercontexttransitioning/containerview.md)
  The view that acts as the superview for the views involved in the transition.
- [func viewController(forKey: UITransitionContextViewControllerKey) -> UIViewController?](uiviewcontrollercontexttransitioning/viewcontroller(forkey:).md)
  Returns a view controller involved in the transition.
- [func view(forKey: UITransitionContextViewKey) -> UIView?](uiviewcontrollercontexttransitioning/view(forkey:).md)
  Returns the specified view involved in the transition.
### Getting the transition frame rectangles
- [func initialFrame(for: UIViewController) -> CGRect](uiviewcontrollercontexttransitioning/initialframe(for:).md)
  Returns the starting frame rectangle for the specified view controller’s view.
- [func finalFrame(for: UIViewController) -> CGRect](uiviewcontrollercontexttransitioning/finalframe(for:).md)
  Returns the ending frame rectangle for the specified view controller’s view.
### Getting the transition behaviors
- [var isAnimated: Bool](uiviewcontrollercontexttransitioning/isanimated.md)
  A Boolean value indicating whether the transition should be animated.
- [var isInteractive: Bool](uiviewcontrollercontexttransitioning/isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var presentationStyle: UIModalPresentationStyle](uiviewcontrollercontexttransitioning/presentationstyle.md)
  Returns the presentation style for the view controller transition.
### Reporting the transition progress
- [func completeTransition(Bool)](uiviewcontrollercontexttransitioning/completetransition(_:).md)
  Notifies the system that the transition animation is done.
- [func updateInteractiveTransition(CGFloat)](uiviewcontrollercontexttransitioning/updateinteractivetransition(_:).md)
  Updates the completion percentage of the transition.
- [func pauseInteractiveTransition()](uiviewcontrollercontexttransitioning/pauseinteractivetransition.md)
  Tells the system to pause the animations.
- [func finishInteractiveTransition()](uiviewcontrollercontexttransitioning/finishinteractivetransition.md)
  Notifies the system that user interactions signaled the completion of the transition.
- [func cancelInteractiveTransition()](uiviewcontrollercontexttransitioning/cancelinteractivetransition.md)
  Notifies the system that user interactions canceled the transition.
- [var transitionWasCancelled: Bool](uiviewcontrollercontexttransitioning/transitionwascancelled.md)
  Returns a Boolean value indicating whether the transition was canceled.
### Getting the rotation factor
- [var targetTransform: CGAffineTransform](uiviewcontrollercontexttransitioning/targettransform.md)
  Returns a transform indicating the amount of rotation being applied during the transition.
### Constants
- [struct UITransitionContextViewControllerKey](uitransitioncontextviewcontrollerkey.md)
  The keys you use to identify the view controllers involved in a transition.
- [struct UITransitionContextViewKey](uitransitioncontextviewkey.md)
  The keys you use to identify the views involved in a transition.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md)
  A set of methods for implementing the animations for a custom view controller transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning)*