# animateTransition(using:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells your animator object to perform the transition animations.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func animateTransition(using transitionContext: any UIViewControllerContextTransitioning)
```

```objc
- (void) animateTransition:(id<UIViewControllerContextTransitioning>) transitionContext;
```

#### Discussion

UIKit calls this method when presenting or dismissing a view controller. Use this method to configure the animations associated with your custom transition. You can use view-based animations or Core Animation to configure your animations.

All animations must take place in the view specified by the [`containerView`](../uiviewcontrollercontexttransitioning/containerview.md) property of `transitionContext`. Add the view being presented (or revealed if the transition involves dismissing a view controller) to the container view’s hierarchy and set up any animations you want to make that view move into position. If you want to draw to the screen directly without a view, use this method to configure a [`CADisplayLink`](../../QuartzCore/cadisplaylink.md) object instead.

You can retrieve the view controllers involved in the transition from the [`viewController(forKey:)`](../uiviewcontrollercontexttransitioning/viewcontroller%28forkey%29.md) method of `transitionContext`. For more information about the information provided by the context object, see [`UIViewControllerContextTransitioning`](../uiviewcontrollercontexttransitioning.md).

## Parameters

- `transitionContext`: The context object containing information about the transition.

## See Also

### Performing a transition
- [func animationEnded(Bool)](./animationended%28_%29.md)
  Tells your animator object that the transition animations have finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/animatetransition(using:))*