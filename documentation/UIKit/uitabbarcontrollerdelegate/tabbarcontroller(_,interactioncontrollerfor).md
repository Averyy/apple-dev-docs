# tabBarController(_:interactionControllerFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called to allow the delegate to return a [`UIViewControllerInteractiveTransitioning`](../uiviewcontrollerinteractivetransitioning.md) delegate object for use during an animated tab bar transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, interactionControllerFor animationController: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

```objc
- (id<UIViewControllerInteractiveTransitioning>) tabBarController:(UITabBarController *) tabBarController interactionControllerForAnimationController:(id<UIViewControllerAnimatedTransitioning>) animationController;
```

## Return Value

The [`UIViewControllerInteractiveTransitioning`](../uiviewcontrollerinteractivetransitioning.md) delegate object responsible for managing the user interaction in an animated tab bar transition.

## Parameters

- `tabBarController`: The tab bar controller participating in the interactive, animated transition.
- `animationController`: The noninteractive animation controller

## See Also

### Supporting custom tab bar transition animations
- [func tabBarController(UITabBarController, animationControllerForTransitionFrom: UIViewController, to: UIViewController) -> (any UIViewControllerAnimatedTransitioning)?](./tabbarcontroller%28_,animationcontrollerfortransitionfrom,to%29.md)
  Called to allow the delegate to return a [`UIViewControllerAnimatedTransitioning`](../uiviewcontrolleranimatedtransitioning.md) delegate object for use during a noninteractive tab bar view controller transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:interactioncontrollerfor:))*