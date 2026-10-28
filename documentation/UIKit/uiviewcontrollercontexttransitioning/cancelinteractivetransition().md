# cancelInteractiveTransition()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the system that user interactions canceled the transition.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func cancelInteractiveTransition()
```

```objc
- (void) cancelInteractiveTransition;
```

## Discussion

While tracking user interactions, gesture recognizers or your interactive animator object should call this method when interactions suggest that the user wants to cancel or abort the view controller transition. For example, if the user reverses the swipe direction and touch events end, suggesting that the user decided against the transition, you would call this method.

Always follow calls to this method with a call to the [`completeTransition(_:)`](./completetransition%28_%29.md) method to finalize the transition.

## See Also

### Reporting the transition progress
- [func completeTransition(Bool)](./completetransition%28_%29.md)
  Notifies the system that the transition animation is done.
- [func updateInteractiveTransition(CGFloat)](./updateinteractivetransition%28_%29.md)
  Updates the completion percentage of the transition.
- [func pauseInteractiveTransition()](./pauseinteractivetransition%28%29.md)
  Tells the system to pause the animations.
- [func finishInteractiveTransition()](./finishinteractivetransition%28%29.md)
  Notifies the system that user interactions signaled the completion of the transition.
- [var transitionWasCancelled: Bool](./transitionwascancelled.md)
  Returns a Boolean value indicating whether the transition was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/cancelinteractivetransition())*