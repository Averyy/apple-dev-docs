# pauseInteractiveTransition()

**Framework**: UIKit  
**Kind**: method  
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
@MainActor
func pauseInteractiveTransition()
```

#### Discussion

You can call this method in the middle of an interruptible animation to pause it.

## See Also

- [func completeTransition(Bool)](uiviewcontrollercontexttransitioning/completetransition(_:).md)
  Notifies the system that the transition animation is done.
- [func updateInteractiveTransition(CGFloat)](uiviewcontrollercontexttransitioning/updateinteractivetransition(_:).md)
  Updates the completion percentage of the transition.
- [func finishInteractiveTransition()](uiviewcontrollercontexttransitioning/finishinteractivetransition.md)
  Notifies the system that user interactions signaled the completion of the transition.
- [func cancelInteractiveTransition()](uiviewcontrollercontexttransitioning/cancelinteractivetransition.md)
  Notifies the system that user interactions canceled the transition.
- [var transitionWasCancelled: Bool](uiviewcontrollercontexttransitioning/transitionwascancelled.md)
  Returns a Boolean value indicating whether the transition was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/pauseinteractivetransition())*