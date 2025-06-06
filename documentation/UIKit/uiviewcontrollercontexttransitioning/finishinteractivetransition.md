# finishInteractiveTransition()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Notifies the system that user interactions signaled the completion of the transition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func finishInteractiveTransition()
```

#### Discussion

While tracking user interactions, gesture recognizers or your interactive animator object should call this method when the interactions suggest that the transition is now complete. For example, if the user swipes a finger, and the touch events indicate that the swipe distance crossed the threshold needed to complete the gesture, call this method when the corresponding touch events end to let the system know that it can now complete the transition.

Always follow calls to this method with a call to the [`completeTransition(_:)`](uiviewcontrollercontexttransitioning/completetransition(_:).md) method to finalize the transition.

## See Also

- [func completeTransition(Bool)](uiviewcontrollercontexttransitioning/completetransition(_:).md)
  Notifies the system that the transition animation is done.
- [func updateInteractiveTransition(CGFloat)](uiviewcontrollercontexttransitioning/updateinteractivetransition(_:).md)
  Updates the completion percentage of the transition.
- [func pauseInteractiveTransition()](uiviewcontrollercontexttransitioning/pauseinteractivetransition.md)
  Tells the system to pause the animations.
- [func cancelInteractiveTransition()](uiviewcontrollercontexttransitioning/cancelinteractivetransition.md)
  Notifies the system that user interactions canceled the transition.
- [var transitionWasCancelled: Bool](uiviewcontrollercontexttransitioning/transitionwascancelled.md)
  Returns a Boolean value indicating whether the transition was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/finishinteractivetransition())*