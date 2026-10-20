# transition(from:to:duration:options:animations:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Transitions between two of the view controller’s child view controllers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration: TimeInterval, options: UIView.AnimationOptions = [], animations: (() -> Void)?, completion: ((Bool) -> Void)? = nil)
```

```objc
- (void) transitionFromViewController:(UIViewController *) fromViewController toViewController:(UIViewController *) toViewController duration:(NSTimeInterval) duration options:(UIViewAnimationOptions) options animations:(void (^)()) animations completion:(void (^)(BOOL finished)) completion;
```

#### Discussion

This method adds the second view controller’s view to the view hierarchy and then performs the animations defined in your animations block. After the animation completes, it removes the first view controller’s view from the view hierarchy.

This method is only intended to be called by an implementation of a custom container view controller. If you override this method, you must call `super` in your implementation.

## Parameters

- `fromViewController`: A view controller whose view is currently visible in the parent’s view hierarchy.
- `toViewController`: A child view controller whose view is not currently in the view hierarchy.
- `duration`: The total duration of the animations, in seconds. If you pass zero, the changes are made without animating them.
- `options`: A mask of options indicating how you want to perform the animations. For a list of valid constants, see [`UIView.AnimationOptions`](../uiview/animationoptions.md).
- `animations`: A block object containing the changes to commit to the views. Here you programmatically change any animatable properties of the views in your view hierarchy. This block takes no parameters and has no return value. This parameter must not be `NULL`.
- `completion`: A block to be called when the animation completes.

  The block takes the following parameters:

  - ***finished***: [`true`](../../Swift/true.md) if the animation finished; [`false`](../../Swift/false.md) if it was skipped.

## See Also

### Managing child view controllers in a custom container
- [var children: [UIViewController]](./children.md)
  An array of view controllers that are children of the current view controller.
- [func addChild(UIViewController)](./addchild%28_%29.md)
  Adds the specified view controller as a child of the current view controller.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the view controller from its parent.
- [var shouldAutomaticallyForwardAppearanceMethods: Bool](./shouldautomaticallyforwardappearancemethods.md)
  Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [func beginAppearanceTransition(Bool, animated: Bool)](./beginappearancetransition%28_,animated%29.md)
  Tells a child controller its appearance is about to change.
- [func endAppearanceTransition()](./endappearancetransition%28%29.md)
  Tells a child controller its appearance has changed.
- [class let hierarchyInconsistencyException: NSExceptionName](./hierarchyinconsistencyexception.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition(from:to:duration:options:animations:completion:))*