# animateAlongsideTransition(in:animation:completion:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Runs the specified animations in a view that’s outside of the designated container view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func animateAlongsideTransition(in view: UIView?, animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the specified animation is successfully queued to run; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Use this method to perform animations that aren’t handled by the animator objects themselves. The animations you specify in the `animation` parameter must all take place in a view descended from the view you specify in the `view` parameter.

The animations in the `animation` parameter are normally performed concurrently with the view controller transition animations. That behavior applies when the animator object’s [`animateTransition(using:)`](uiviewcontrolleranimatedtransitioning/animatetransition(using:).md) method is implemented using [`UIView`](uiview.md)-based animations. If the animator object uses Core Animation to animate the layer contents directly, your animations are run shortly after the animateTransition: method returns.

This method returns [`false`](https://developer.apple.com/documentation/Swift/false) when the block in the `animation` parameter can’t be queued to run. The completion block can still run even when this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `view`: The view (or one of its ancestors) in which the specified animations take place. This parameter must not be  .
- `animation`: The block has no return value and takes the following parameter:
- `completion`: The block of code to execute after the transition finishes. You may specify   for this parameter. The block has no return value and takes the following parameter:

## See Also

- [func animate(alongsideTransition: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool](uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:).md)
  Runs the specified animations at the same time as the view controller transition animations.
- [func notifyWhenInteractionChanges((any UIViewControllerTransitionCoordinatorContext) -> Void)](uiviewcontrollertransitioncoordinator/notifywheninteractionchanges(_:).md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.
- [func notifyWhenInteractionEnds((any UIViewControllerTransitionCoordinatorContext) -> Void)](uiviewcontrollertransitioncoordinator/notifywheninteractionends(_:).md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:))*