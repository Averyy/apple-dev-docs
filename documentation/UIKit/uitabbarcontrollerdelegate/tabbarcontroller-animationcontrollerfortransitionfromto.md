# tabBarController(_:animationControllerForTransitionFrom:to:)

**Framework**: UIKit  
**Kind**: method

Called to allow the delegate to return a [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) delegate object for use during a noninteractive tab bar view controller transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func tabBarController(_ tabBarController: UITabBarController, animationControllerForTransitionFrom fromVC: UIViewController, to toVC: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?
```

#### Return Value

The [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) delegate object responsible for managing the tab bar view controller transition animation.

## Parameters

- `tabBarController`: The tab bar controller whose view controller is transitioning.
- `fromVC`: The currently visible view controller.
- `toVC`: The view controller intended to be visible after the transition ends.

## See Also

- [func tabBarController(UITabBarController, interactionControllerFor: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?](uitabbarcontrollerdelegate/tabbarcontroller(_:interactioncontrollerfor:).md)
  Called to allow the delegate to return a [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md) delegate object for use during an animated tab bar transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:animationcontrollerfortransitionfrom:to:))*