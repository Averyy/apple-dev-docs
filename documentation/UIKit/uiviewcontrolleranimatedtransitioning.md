# UIViewControllerAnimatedTransitioning

**Framework**: UIKit  
**Kind**: protocol

A set of methods for implementing the animations for a custom view controller transition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIViewControllerAnimatedTransitioning : NSObjectProtocol
```

#### Overview

The methods in this protocol let you define an animator object, which creates the animations for transitioning a view controller on or off screen in a fixed amount of time. The animations you create using this protocol must not be interactive. To create interactive transitions, you must combine your animator object with another object that controls the timing of your animations.

In your animator object, implement the [`transitionDuration(using:)`](uiviewcontrolleranimatedtransitioning/transitionduration(using:).md) method to specify the duration of your transition and implement the [`animateTransition(using:)`](uiviewcontrolleranimatedtransitioning/animatetransition(using:).md) method to create the animations themselves. Information about the objects involved in the transition is passed to your [`animateTransition(using:)`](uiviewcontrolleranimatedtransitioning/animatetransition(using:).md) method in the form of a context object. Use the information provided by that object to move the target view controller’s view on or off screen over the specified duration.

Create your animator object from a transitioning delegate — an object that conforms to the [`UIViewControllerTransitioningDelegate`](uiviewcontrollertransitioningdelegate.md) protocol. When presenting a view controller, set the presentation style to [`UIModalPresentationStyle.custom`](uimodalpresentationstyle/custom.md) and assign your transitioning delegate to the view controller’s [`transitioningDelegate`](uiviewcontroller/transitioningdelegate.md) property. The view controller retrieves your animator object from the transitioning delegate and uses it to perform the animations. You can provide separate animator objects for presenting and dismissing the view controller.

To add user interaction to a view controller transition, you must use an animator object together with an ** **— a custom object that adopts the [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md) protocol. For more on defining interactive transitions, see [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md).

## Topics

### Performing a transition
- [func animateTransition(using: any UIViewControllerContextTransitioning)](uiviewcontrolleranimatedtransitioning/animatetransition(using:).md)
  Tells your animator object to perform the transition animations.
- [func animationEnded(Bool)](uiviewcontrolleranimatedtransitioning/animationended(_:).md)
  Tells your animator object that the transition animations have finished.
### Reporting transition duration
- [func transitionDuration(using: (any UIViewControllerContextTransitioning)?) -> TimeInterval](uiviewcontrolleranimatedtransitioning/transitionduration(using:).md)
  Asks your animator object for the duration (in seconds) of the transition animation.
### Returning an interruptible animator
- [func interruptibleAnimator(using: any UIViewControllerContextTransitioning) -> any UIViewImplicitlyAnimating](uiviewcontrolleranimatedtransitioning/interruptibleanimator(using:).md)
  Returns the interruptible animator to use during the transition.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIDocumentBrowserTransitionController](uidocumentbrowsertransitioncontroller.md)
- [UISearchController](uisearchcontroller.md)

## See Also

- [protocol UIViewControllerContextTransitioning](uiviewcontrollercontexttransitioning.md)
  A set of methods that provide contextual information for transition animations between view controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning)*