# pauseInteractiveTransition()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the system to pause the animations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func pauseInteractiveTransition()
```

```objc
- (void) pauseInteractiveTransition;
```

#### Discussion

You can call this method in the middle of an interruptible animation to pause it.

## See Also

### Reporting the transition progress
- [func completeTransition(Bool)](./completetransition%28_%29.md)
  Notifies the system that the transition animation is done.
- [func updateInteractiveTransition(CGFloat)](./updateinteractivetransition%28_%29.md)
  Updates the completion percentage of the transition.
- [func finishInteractiveTransition()](./finishinteractivetransition%28%29.md)
  Notifies the system that user interactions signaled the completion of the transition.
- [func cancelInteractiveTransition()](./cancelinteractivetransition%28%29.md)
  Notifies the system that user interactions canceled the transition.
- [var transitionWasCancelled: Bool](./transitionwascancelled.md)
  Returns a Boolean value indicating whether the transition was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/pauseinteractivetransition())*