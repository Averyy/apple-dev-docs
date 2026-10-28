# animateAlongsideTransition(in:animation:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Runs the specified animations in a view that’s outside of the designated container view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func animateAlongsideTransition(in view: UIView?, animation: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)? = nil) -> Bool
```

```objc
- (BOOL) animateAlongsideTransitionInView:(UIView *) view animation:(void (^)(id<UIViewControllerTransitionCoordinatorContext>context)) animation completion:(void (^)(id<UIViewControllerTransitionCoordinatorContext>context)) completion;
```

## Return Value

[`true`](../../Swift/true.md) if the specified animation is successfully queued to run; otherwise [`false`](../../Swift/false.md).

## Discussion

Use this method to perform animations that aren’t handled by the animator objects themselves. The animations you specify in the `animation` parameter must all take place in a view descended from the view you specify in the `view` parameter.

The animations in the `animation` parameter are normally performed concurrently with the view controller transition animations. That behavior applies when the animator object’s [`animateTransition(using:)`](../uiviewcontrolleranimatedtransitioning/animatetransition%28using%29.md) method is implemented using [`UIView`](../uiview.md)-based animations. If the animator object uses Core Animation to animate the layer contents directly, your animations are run shortly after the animateTransition: method returns.

This method returns [`false`](../../Swift/false.md) when the block in the `animation` parameter can’t be queued to run. The completion block can still run even when this method returns [`false`](../../Swift/false.md).

## Parameters

- `view`: The view (or one of its ancestors) in which the specified animations take place. This parameter must not be `nil`.
- `animation`: A block containing the animations you want to perform. These animations run in the same context as the transition animations and therefore have the same default attributes. You may specify `nil` for this parameter.

  The block has no return value and takes the following parameter:

  - **context**: The contextual information for performing the animations. Use this object to get the animation-related information. For more information, see [`UIViewControllerTransitionCoordinatorContext`](../uiviewcontrollertransitioncoordinatorcontext.md).
- `completion`: The block of code to execute after the transition finishes. You may specify `nil` for this parameter. The block has no return value and takes the following parameter:

  - **context**: The contextual information for performing the animations. Use this object to get the animation-related information. For more information, see [`UIViewControllerTransitionCoordinatorContext`](../uiviewcontrollertransitioncoordinatorcontext.md).

## See Also

### Responding to view controller transition progress
- [func animate(alongsideTransition: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?, completion: ((any UIViewControllerTransitionCoordinatorContext) -> Void)?) -> Bool](./animate%28alongsidetransition,completion%29.md)
  Runs the specified animations at the same time as the view controller transition animations.
- [func notifyWhenInteractionChanges((any UIViewControllerTransitionCoordinatorContext) -> Void)](./notifywheninteractionchanges%28_%29.md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.
- [func notifyWhenInteractionEnds((any UIViewControllerTransitionCoordinatorContext) -> Void)](./notifywheninteractionends%28_%29.md)
  Registers a block to be executed when a transition changes from interactive to non-interactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:))*