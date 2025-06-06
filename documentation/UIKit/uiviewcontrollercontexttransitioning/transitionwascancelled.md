# transitionWasCancelled

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

Returns a Boolean value indicating whether the transition was canceled.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var transitionWasCancelled: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the transition was canceled or [`false`](https://developer.apple.com/documentation/swift/false) if it is ongoing or finished normally.

#### Discussion

You can call this method from your animator object to determine whether the transition has been canceled. Calling the [`cancelInteractiveTransition()`](uiviewcontrollercontexttransitioning/cancelinteractivetransition().md) method causes this method to return [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func completeTransition(Bool)](uiviewcontrollercontexttransitioning/completetransition(_:).md)
  Notifies the system that the transition animation is done.
- [func updateInteractiveTransition(CGFloat)](uiviewcontrollercontexttransitioning/updateinteractivetransition(_:).md)
  Updates the completion percentage of the transition.
- [func pauseInteractiveTransition()](uiviewcontrollercontexttransitioning/pauseinteractivetransition.md)
  Tells the system to pause the animations.
- [func finishInteractiveTransition()](uiviewcontrollercontexttransitioning/finishinteractivetransition.md)
  Notifies the system that user interactions signaled the completion of the transition.
- [func cancelInteractiveTransition()](uiviewcontrollercontexttransitioning/cancelinteractivetransition.md)
  Notifies the system that user interactions canceled the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/transitionwascancelled)*