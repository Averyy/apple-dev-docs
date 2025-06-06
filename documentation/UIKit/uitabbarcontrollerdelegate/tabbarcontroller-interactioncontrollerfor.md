# tabBarController(_:interactionControllerFor:)

**Framework**: UIKit  
**Kind**: method

Called to allow the delegate to return a [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md) delegate object for use during an animated tab bar transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func tabBarController(_ tabBarController: UITabBarController, interactionControllerFor animationController: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

#### Return Value

The [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md) delegate object responsible for managing the user interaction in an animated tab bar transition.

## Parameters

- `tabBarController`: The tab bar controller participating in the interactive, animated transition.
- `animationController`: The noninteractive animation controller

## See Also

- [func tabBarController(UITabBarController, animationControllerForTransitionFrom: UIViewController, to: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](uitabbarcontrollerdelegate/tabbarcontroller(_:animationcontrollerfortransitionfrom:to:).md)
  Called to allow the delegate to return a [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) delegate object for use during a noninteractive tab bar view controller transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:interactioncontrollerfor:))*