# completeTransition(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the system that the transition animation is done.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func completeTransition(_ didComplete: Bool)
```

```objc
- (void) completeTransition:(BOOL) didComplete;
```

#### Discussion

You must call this method after your animations have completed to notify the system that the transition animation is done. The parameter you pass must indicate whether the animations completed successfully. For interactive animations, you must call this method in addition to the [`finishInteractiveTransition()`](./finishinteractivetransition%28%29.md) or [`cancelInteractiveTransition()`](./cancelinteractivetransition%28%29.md) method. The best place to call this method is in the completion block of your animations.

The default implementation of this method calls the animator object’s [`animationEnded(_:)`](../uiviewcontrolleranimatedtransitioning/animationended%28_%29.md) method to give it a chance to perform any last minute cleanup.

## Parameters

- `didComplete`: [`true`](../../Swift/true.md) if the transition to the presented view controller completed successfully or [`false`](../../Swift/false.md) if the original view controller is still being displayed.

## See Also

### Reporting the transition progress
- [func updateInteractiveTransition(CGFloat)](./updateinteractivetransition%28_%29.md)
  Updates the completion percentage of the transition.
- [func pauseInteractiveTransition()](./pauseinteractivetransition%28%29.md)
  Tells the system to pause the animations.
- [func finishInteractiveTransition()](./finishinteractivetransition%28%29.md)
  Notifies the system that user interactions signaled the completion of the transition.
- [func cancelInteractiveTransition()](./cancelinteractivetransition%28%29.md)
  Notifies the system that user interactions canceled the transition.
- [var transitionWasCancelled: Bool](./transitionwascancelled.md)
  Returns a Boolean value indicating whether the transition was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/completetransition(_:))*