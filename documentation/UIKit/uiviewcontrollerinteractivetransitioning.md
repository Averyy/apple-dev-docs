# UIViewControllerInteractiveTransitioning

**Framework**: UIKit  
**Kind**: protocol

A set of methods that enable an object (such as a navigation controller) to drive a view controller transition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIViewControllerInteractiveTransitioning : NSObjectProtocol
```

#### Overview

An  (which is the term for an object that supports this protocol) can respond to touch events, or to time-varying programmatic input, by speeding up, slowing down, or even reversing the progress of a view controller transition. For example, an interactive transition on a navigation controller could respond to a swipe gesture by moving a view controller onto or off of the navigation stack.

To support an interactive view controller transition, you must also provide a transition animator delegate, which is a custom object that adopts the [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) protocol. The transition delegate and the transition animator can, if you wish, be defined within a single custom class, but the class must adopt both protocols.

If you instead want to provide a fixed-duration animated view controller transition — one that doesn’t support user interaction — use a transition animator delegate on its own. Refer to [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md).

For the methods you can call to retrieve view transition context information from within your [`startInteractiveTransition(_:)`](uiviewcontrollerinteractivetransitioning/startinteractivetransition(_:).md) method, refer to [`UIViewControllerContextTransitioning`](uiviewcontrollercontexttransitioning.md).

## Topics

### Starting an interactive transition
- [func startInteractiveTransition(any UIViewControllerContextTransitioning)](uiviewcontrollerinteractivetransitioning/startinteractivetransition(_:).md)
  Called when the system needs to set up the interactive portions of a view controller transition and start the animations.
- [var wantsInteractiveStart: Bool](uiviewcontrollerinteractivetransitioning/wantsinteractivestart.md)
  A Boolean value indicating whether the transition is interactive when it starts.
### Providing a transition’s completion characteristics
- [var completionCurve: UIView.AnimationCurve](uiviewcontrollerinteractivetransitioning/completioncurve.md)
  Called when the system needs the animation completion curve for an interactive view controller transition.
- [var completionSpeed: CGFloat](uiviewcontrollerinteractivetransitioning/completionspeed.md)
  Called when the system needs the speed at which to complete an interactive transition, after the interactive portion is finished.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIPercentDrivenInteractiveTransition](uipercentdriveninteractivetransition.md)

## See Also

- [class UIPercentDrivenInteractiveTransition](uipercentdriveninteractivetransition.md)
  An object that drives an interactive animation between one view controller and another.
- [protocol UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md)
  An interface for modifying an animation while it’s running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning)*