# animate(alongsideTransition:completion:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Runs the specified animations at the same time as the view controller transition animations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func animate(alongsideTransition animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the animations were successfully queued to run or [`false`](https://developer.apple.com/documentation/Swift/false) if they were not.

#### Discussion

Use this method to perform animations that aren’t handled by the animator objects themselves. All of the animations you specify must occur inside the animation context’s container view (or one of its descendants). Use the [`containerView`](uiviewcontrollertransitioncoordinatorcontext/containerview.md) property of the context object to get the container view. To perform animations in a view that doesn’t descend from the container view, use the [`animateAlongsideTransition(in:animation:completion:)`](uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:).md) method instead.

The animations in the `animation` parameter are normally performed concurrently with the view controller transition animations. That behavior applies when the animator object’s [`animateTransition(using:)`](uiviewcontrolleranimatedtransitioning/animatetransition(using:).md) method is implemented using [`UIView`](uiview.md)-based animations. If the animator object uses Core Animation to animate the layer contents directly, your animations are run shortly after the animateTransition: method returns.

This method returns [`false`](https://developer.apple.com/documentation/Swift/false) when the block in the `animation` parameter can’t be queued to run. The completion block can still run even when this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `animation`: The animation you specify must take place in a view descended from the container view.
- `completion`: The block of code to execute after the transition finishes. You may specify   for this parameter. The block has no return value and takes the following parameter:

## See Also

- [func animateAlongsideTransition(in: UIView?, animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool](uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:).md)
  Runs the specified animations in a view that’s outside of the designated container view.
- [func notifyWhenInteractionChanges((any UIViewControllerTransitionCoordinatorContext) -> Void)](uiviewcontrollertransitioncoordinator/notifywheninteractionchanges(_:).md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.
- [func notifyWhenInteractionEnds((any UIViewControllerTransitionCoordinatorContext) -> Void)](uiviewcontrollertransitioncoordinator/notifywheninteractionends(_:).md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:))*