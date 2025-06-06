# updateInteractiveTransition(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Updates the completion percentage of the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateInteractiveTransition(_ percentComplete: CGFloat)
```

#### Discussion

While tracking user events, gesture recognizers or your interactive animator objects should call this method regularly to update the progress toward completing the transition. If, during tracking, the interactions cross a threshold that you consider signifies the completion or cancellation of the transition, stop tracking events and call the [`finishInteractiveTransition()`](uiviewcontrollercontexttransitioning/finishinteractivetransition().md) or [`cancelInteractiveTransition()`](uiviewcontrollercontexttransitioning/cancelinteractivetransition().md) method.

## See Also

- [func completeTransition(Bool)](uiviewcontrollercontexttransitioning/completetransition(_:).md)
  Notifies the system that the transition animation is done.
- [func pauseInteractiveTransition()](uiviewcontrollercontexttransitioning/pauseinteractivetransition.md)
  Tells the system to pause the animations.
- [func finishInteractiveTransition()](uiviewcontrollercontexttransitioning/finishinteractivetransition.md)
  Notifies the system that user interactions signaled the completion of the transition.
- [func cancelInteractiveTransition()](uiviewcontrollercontexttransitioning/cancelinteractivetransition.md)
  Notifies the system that user interactions canceled the transition.
- [var transitionWasCancelled: Bool](uiviewcontrollercontexttransitioning/transitionwascancelled.md)
  Returns a Boolean value indicating whether the transition was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/updateinteractivetransition(_:))*