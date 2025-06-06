# View controller transitions

**Framework**: UIKit

Define custom transitions from one view controller to another.

## Topics

### Essentials
- [Enhancing your app with fluid transitions](enhancing-your-app-with-fluid-transitions.md)
  Use the fluid zoom transition to provide a continuously interactive and responsive experience in your app.
### Animation delegate
- [protocol UIViewControllerTransitioningDelegate](uiviewcontrollertransitioningdelegate.md)
  A set of methods that vend objects used to manage a fixed-length or interactive transition between view controllers.
### Non-interactive transitions
- [protocol UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md)
  A set of methods for implementing the animations for a custom view controller transition.
- [protocol UIViewControllerContextTransitioning](uiviewcontrollercontexttransitioning.md)
  A set of methods that provide contextual information for transition animations between view controllers.
### Interactive transitions
- [class UIPercentDrivenInteractiveTransition](uipercentdriveninteractivetransition.md)
  An object that drives an interactive animation between one view controller and another.
- [protocol UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md)
  A set of methods that enable an object (such as a navigation controller) to drive a view controller transition.
- [protocol UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md)
  An interface for modifying an animation while it’s running.
### Transition coordinators
- [protocol UIViewControllerTransitionCoordinator](uiviewcontrollertransitioncoordinator.md)
  A set of methods that provides support for animations associated with a view controller transition.
- [protocol UIViewControllerTransitionCoordinatorContext](uiviewcontrollertransitioncoordinatorcontext.md)
  A set of methods that provides information about an in-progress view controller transition.

## See Also

- [Property-based animations](property-based-animations.md)
  Create animations by changing the properties of a view.
- [Unifying your app’s animations](../SwiftUI/Unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [Optimizing ProMotion refresh rates for iPhone 13 Pro and iPad Pro](../QuartzCore/optimizing-promotion-refresh-rates-for-iphone-13-pro-and-ipad-pro.md)
  Provide custom animated content for ProMotion displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/view-controller-transitions)*