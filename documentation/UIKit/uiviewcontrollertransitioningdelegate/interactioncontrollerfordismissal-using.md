# interactionControllerForDismissal(using:)

**Framework**: UIKit  
**Kind**: method

Asks your delegate for the interactive animator object to use when dismissing a view controller.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional func interactionControllerForDismissal(using animator: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?
```

#### Return Value

The animator object that implements the code needed specifically to manage interactive transitions or `nil` if you do not want to support interactive transitions.

#### Discussion

Use this method to create and return an object that implements the methods of the [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md) protocol. The implementation of that protocol should configure the event-handling code required to manage the disappearance of the target view controller. You may return `nil` from this method if you do not want to the animations to be interactive.

> ❗ **Important**:  If you implement this method, you must also implement the [`animationController(forDismissed:)`](uiviewcontrollertransitioningdelegate/animationcontroller(fordismissed:).md) method and use it to return a custom transition animator object. If the [`animationController(forDismissed:)`](uiviewcontrollertransitioningdelegate/animationcontroller(fordismissed:).md) method returns `nil`, UIKit does not call this method.

 If you implement this method, you must also implement the [`animationController(forDismissed:)`](uiviewcontrollertransitioningdelegate/animationcontroller(fordismissed:).md) method and use it to return a custom transition animator object. If the [`animationController(forDismissed:)`](uiviewcontrollertransitioningdelegate/animationcontroller(fordismissed:).md) method returns `nil`, UIKit does not call this method.

For more information on implementing an interactive animator object, see [`UIViewControllerInteractiveTransitioning`](uiviewcontrollerinteractivetransitioning.md).

## Parameters

- `animator`: The transition animator object returned by your   method.

## See Also

- [func interactionControllerForPresentation(using: any UIViewControllerAnimatedTransitioning) -> (any UIViewControllerInteractiveTransitioning)?](uiviewcontrollertransitioningdelegate/interactioncontrollerforpresentation(using:).md)
  Asks your delegate for the interactive animator object to use when presenting a view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioningdelegate/interactioncontrollerfordismissal(using:))*