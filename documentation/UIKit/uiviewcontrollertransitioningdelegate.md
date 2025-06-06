# UIViewControllerTransitioningDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods that vend objects used to manage a fixed-length or interactive transition between view controllers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIViewControllerTransitioningDelegate : NSObjectProtocol
```

#### Overview

When you want to present a view controller using a custom modal presentation type, set its [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) property to `custom` and assign an object that conforms to this protocol to its [`transitioningDelegate`](uiviewcontroller/transitioningdelegate.md) property. When you present that view controller, UIKit queries your transitioning delegate for the objects to use when animating the view controller into position.

When implementing your transitioning delegate object, you can return different animator objects depending on whether a view controller is being presented or dismissed. All transitions use a —an object that conforms to the [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) protocol—to implement the basic animations. A transition animator object performs a set of animations over a finite period of time. If you want to use touch input or other user interactions to control the timing of the animation, you can also provide an —an object that conforms to the [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md) protocol—to update the progress of the animations. You can provide separate animator objects for presenting and dismissing the view controller.

For custom modal transition styles, you can provide a [`UIPresentationController`](uipresentationcontroller.md) object in addition to the animator objects. The system creates your presentation controller before presenting the view controller and keeps a reference to that object until the view controller is dismissed. Because its existence extends beyond the lifespan of either animator object, you can use the presentation controller to coordinate aspects of the presentation or dismissal process that would be difficult to do otherwise. For example, if your custom transition style involves displaying a separate shadow view as a backdrop to the view controller’s content, the presentation controller can create the shadow view and show it and hide it at the appropriate times.

## Topics

### Getting the transition animator objects
- [func animationController(forPresented: UIViewController, presenting: UIViewController, source: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](uiviewcontrollertransitioningdelegate/animationcontroller(forpresented:presenting:source:).md)
  Asks your delegate for the transition animator object to use when presenting a view controller.
- [func animationController(forDismissed: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](uiviewcontrollertransitioningdelegate/animationcontroller(fordismissed:).md)
  Asks your delegate for the transition animator object to use when dismissing a view controller.
### Getting the interactive animator objects
- [func interactionControllerForPresentation(using: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?](uiviewcontrollertransitioningdelegate/interactioncontrollerforpresentation(using:).md)
  Asks your delegate for the interactive animator object to use when presenting a view controller.
- [func interactionControllerForDismissal(using: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?](uiviewcontrollertransitioningdelegate/interactioncontrollerfordismissal(using:).md)
  Asks your delegate for the interactive animator object to use when dismissing a view controller.
### Getting the custom presentation controller
- [func presentationController(forPresented: UIViewController, presenting: UIViewController?, source: UIViewController) -> UIPresentationController?](uiviewcontrollertransitioningdelegate/presentationcontroller(forpresented:presenting:source:).md)
  Asks your delegate for the custom presentation controller to use for managing the view hierarchy when presenting a view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UISearchController](uisearchcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate)*