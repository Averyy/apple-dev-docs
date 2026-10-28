# transitionWasCancelled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns a Boolean value indicating whether the transition was canceled.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var transitionWasCancelled: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL transitionWasCancelled;
```

## Return Value

[`true`](../../Swift/true.md) if the transition was canceled or [`false`](../../Swift/false.md) if it is ongoing or finished normally.

## Discussion

You can call this method from your animator object to determine whether the transition has been canceled. Calling the [`cancelInteractiveTransition()`](./cancelinteractivetransition%28%29.md) method causes this method to return [`true`](../../Swift/true.md).

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
- [func cancelInteractiveTransition()](./cancelinteractivetransition%28%29.md)
  Notifies the system that user interactions canceled the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/transitionwascancelled)*