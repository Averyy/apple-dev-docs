# startInteractiveTransition(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Called when the system needs to set up the interactive portions of a view controller transition and start the animations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func startInteractiveTransition(_ transitionContext: any UIViewControllerContextTransitioning)
```

#### Discussion

Your implementation of this method should use the data in the `transitionContext` parameter to configure user interactivity for the transition and then start the animations. While tracking user interactions, your event handling code should regularly call the context object’s [`updateInteractiveTransition(_:)`](uiviewcontrollercontexttransitioning/updateinteractivetransition(_:).md) method to report on how much of the transition is now complete. If events indicate that the user has canceled the transition, call the [`cancelInteractiveTransition()`](uiviewcontrollercontexttransitioning/cancelinteractivetransition().md) method. If events indicate that the transition has finished, call the [`finishInteractiveTransition()`](uiviewcontrollercontexttransitioning/finishinteractivetransition().md) method.

## Parameters

- `transitionContext`: The context object containing information about the transition.

## See Also

- [var wantsInteractiveStart: Bool](uiviewcontrollerinteractivetransitioning/wantsinteractivestart.md)
  A Boolean value indicating whether the transition is interactive when it starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/startinteractivetransition(_:))*