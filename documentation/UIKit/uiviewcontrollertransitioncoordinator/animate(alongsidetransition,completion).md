# animate(alongsideTransition:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Runs the specified animations at the same time as the view controller transition animations.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func animate(alongsideTransition animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)? = nil) -> Bool
```

```objc
- (BOOL) animateAlongsideTransition:(void (^)(id<UIViewControllerTransitionCoordinatorContext>context)) animation completion:(void (^)(id<UIViewControllerTransitionCoordinatorContext>context)) completion;
```

#### Return Value

[`true`](../../Swift/true.md) if the animations were successfully queued to run or [`false`](../../Swift/false.md) if they were not.

#### Discussion

Use this method to perform animations that aren’t handled by the animator objects themselves. All of the animations you specify must occur inside the animation context’s container view (or one of its descendants). Use the [`containerView`](../uiviewcontrollertransitioncoordinatorcontext/containerview.md) property of the context object to get the container view. To perform animations in a view that doesn’t descend from the container view, use the [`animateAlongsideTransition(in:animation:completion:)`](./animatealongsidetransition%28in,animation,completion%29.md) method instead.

The animations in the `animation` parameter are normally performed concurrently with the view controller transition animations. That behavior applies when the animator object’s [`animateTransition(using:)`](../uiviewcontrolleranimatedtransitioning/animatetransition%28using%29.md) method is implemented using [`UIView`](../uiview.md)-based animations. If the animator object uses Core Animation to animate the layer contents directly, your animations are run shortly after the animateTransition: method returns.

This method returns [`false`](../../Swift/false.md) when the block in the `animation` parameter can’t be queued to run. The completion block can still run even when this method returns [`false`](../../Swift/false.md).

## Parameters

- `animation`: A block containing the animations you want to perform. These animations run in the same context as the transition animations and therefore have the same default attributes. You may specify `nil` for this parameter.

  The block has no return value and takes the following parameter:

  - **context**: The contextual information for performing the animations. Use this object to get the animation-related information, including the container view in which to run your animations. For more information, see [`UIViewControllerTransitionCoordinatorContext`](../uiviewcontrollertransitioncoordinatorcontext.md).

  The animation you specify must take place in a view descended from the container view.
- `completion`: The block of code to execute after the transition finishes. You may specify `nil` for this parameter. The block has no return value and takes the following parameter:

  - **context**: The contextual information for performing the animations. Use this object to get the animation-related information, including the container view in which to run your animations. For more information, see [`UIViewControllerTransitionCoordinatorContext`](../uiviewcontrollertransitioncoordinatorcontext.md).

## See Also

### Responding to view controller transition progress
- [func animateAlongsideTransition(in: UIView?, animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool](./animatealongsidetransition%28in,animation,completion%29.md)
  Runs the specified animations in a view that’s outside of the designated container view.
- [func notifyWhenInteractionChanges((any UIViewControllerTransitionCoordinatorContext) -> Void)](./notifywheninteractionchanges%28_%29.md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.
- [func notifyWhenInteractionEnds((any UIViewControllerTransitionCoordinatorContext) -> Void)](./notifywheninteractionends%28_%29.md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:))*