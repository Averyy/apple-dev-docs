# UIViewControllerTransitionCoordinatorContext

**Framework**: UIKit  
**Kind**: protocol

A set of methods that provides information about an in-progress view controller transition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIViewControllerTransitionCoordinatorContext : NSObjectProtocol
```

#### Overview

Don’t adopt this protocol in your own classes. UIKit creates an object that adopts this protocol and makes it available to your code when you animate changes using a transition coordinator object.

A transition coordinator context provides most of the same information as an object that adopts the [`UIViewControllerContextTransitioning`](uiviewcontrollercontexttransitioning.md) protocol. You use this contextual information to determine the animation parameters, such as the view in which the animations take place, whether the transition is interactive, or whether the transition was the result of an interface orientation change. You then apply that information to the animations you create.

Most animations take place in the view returned by the [`containerView`](uiviewcontrollertransitioncoordinatorcontext/containerview.md) method. And at the time your animation blocks are executed, the view hierarchy already contains the view of the  view controller. You can use your animation blocks to animate additional content in that same container view or you can animate content in an entirely different view.

## Topics

### Getting the views and view controllers
- [func viewController(forKey: UITransitionContextViewControllerKey) -> UIViewController?](uiviewcontrollertransitioncoordinatorcontext/viewcontroller(forkey:).md)
  Returns the view controllers involved in the transition.
- [func view(forKey: UITransitionContextViewKey) -> UIView?](uiviewcontrollertransitioncoordinatorcontext/view(forkey:).md)
  Returns the specified view involved in the transition.
- [var containerView: UIView](uiviewcontrollertransitioncoordinatorcontext/containerview.md)
  Returns the view in which the transition takes place.
### Getting the behavior attributes
- [var presentationStyle: UIModalPresentationStyle](uiviewcontrollertransitioncoordinatorcontext/presentationstyle.md)
  The presentation style to use for the transition.
- [var transitionDuration: TimeInterval](uiviewcontrollertransitioncoordinatorcontext/transitionduration.md)
  Returns the noninteractive duration of a transition.
- [var completionCurve: UIView.AnimationCurve](uiviewcontrollertransitioncoordinatorcontext/completioncurve.md)
  Returns the completion curve associated with the transition.
- [var completionVelocity: CGFloat](uiviewcontrollertransitioncoordinatorcontext/completionvelocity.md)
  Returns the starting velocity to use for any final animations.
- [var percentComplete: CGFloat](uiviewcontrollertransitioncoordinatorcontext/percentcomplete.md)
  Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.
### Getting the transition state
- [var initiallyInteractive: Bool](uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive.md)
  A Boolean value indicating whether the transition started as an interactive transition.
- [var isInteractive: Bool](uiviewcontrollertransitioncoordinatorcontext/isinteractive.md)
  A Boolean value indicating whether the transition is currently interactive.
- [var isAnimated: Bool](uiviewcontrollertransitioncoordinatorcontext/isanimated.md)
  A Boolean value indicating whether the transition is explicitly animated.
- [var isCancelled: Bool](uiviewcontrollertransitioncoordinatorcontext/iscancelled.md)
  A Boolean value indicating whether an interactive transition was canceled.
- [var isInterruptible: Bool](uiviewcontrollertransitioncoordinatorcontext/isinterruptible.md)
  A Boolean value indicating whether the transition animations can be interrupted.
### Getting the rotation factor
- [var targetTransform: CGAffineTransform](uiviewcontrollertransitioncoordinatorcontext/targettransform.md)
  Returns a transform indicating the amount of rotation being applied during the transition.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UIViewControllerTransitionCoordinator](uiviewcontrollertransitioncoordinator.md)

## See Also

- [protocol UIViewControllerTransitionCoordinator](uiviewcontrollertransitioncoordinator.md)
  A set of methods that provides support for animations associated with a view controller transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext)*