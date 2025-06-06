# completeTransition(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Notifies the system that the transition animation is done.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func completeTransition(_ didComplete: Bool)
```

#### Discussion

You must call this method after your animations have completed to notify the system that the transition animation is done. The parameter you pass must indicate whether the animations completed successfully. For interactive animations, you must call this method in addition to the [`finishInteractiveTransition()`](uiviewcontrollercontexttransitioning/finishinteractivetransition().md) or [`cancelInteractiveTransition()`](uiviewcontrollercontexttransitioning/cancelinteractivetransition().md) method. The best place to call this method is in the completion block of your animations.

The default implementation of this method calls the animator object’s [`animationEnded(_:)`](uiviewcontrolleranimatedtransitioning/animationended(_:).md) method to give it a chance to perform any last minute cleanup.

## Parameters

- `didComplete`:   if the transition to the presented view controller completed successfully or   if the original view controller is still being displayed.

## See Also

- [func updateInteractiveTransition(CGFloat)](uiviewcontrollercontexttransitioning/updateinteractivetransition(_:).md)
  Updates the completion percentage of the transition.
- [func pauseInteractiveTransition()](uiviewcontrollercontexttransitioning/pauseinteractivetransition.md)
  Tells the system to pause the animations.
- [func finishInteractiveTransition()](uiviewcontrollercontexttransitioning/finishinteractivetransition.md)
  Notifies the system that user interactions signaled the completion of the transition.
- [func cancelInteractiveTransition()](uiviewcontrollercontexttransitioning/cancelinteractivetransition.md)
  Notifies the system that user interactions canceled the transition.
- [var transitionWasCancelled: Bool](uiviewcontrollercontexttransitioning/transitionwascancelled.md)
  Returns a Boolean value indicating whether the transition was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/completetransition(_:))*