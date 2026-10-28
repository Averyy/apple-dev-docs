# beginAppearanceTransition(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells a child controller its appearance is about to change.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func beginAppearanceTransition(_ isAppearing: Bool, animated: Bool)
```

```objc
- (void) beginAppearanceTransition:(BOOL) isAppearing animated:(BOOL) animated;
```

## Discussion

If you are implementing a custom container controller, use this method to tell the child that its views are about to appear or disappear. Do not invoke [`viewWillAppear(_:)`](./viewwillappear%28_%29.md), [`viewWillDisappear(_:)`](./viewwilldisappear%28_%29.md), [`viewDidAppear(_:)`](./viewdidappear%28_%29.md), or [`viewDidDisappear(_:)`](./viewdiddisappear%28_%29.md) directly.

## Parameters

- `isAppearing`: [`true`](../../Swift/true.md) if the child view controller’s view is about to be added to the view hierarchy, [`false`](../../Swift/false.md) if it is being removed.
- `animated`: If [`true`](../../Swift/true.md), the transition is being animated.

## See Also

### Managing child view controllers in a custom container
- [var children: [UIViewController]](./children.md)
  An array of view controllers that are children of the current view controller.
- [func addChild(UIViewController)](./addchild%28_%29.md)
  Adds the specified view controller as a child of the current view controller.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the view controller from its parent.
- [func transition(from: UIViewController, to: UIViewController, duration: TimeInterval, options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](./transition%28from,to,duration,options,animations,completion%29.md)
  Transitions between two of the view controller’s child view controllers.
- [var shouldAutomaticallyForwardAppearanceMethods: Bool](./shouldautomaticallyforwardappearancemethods.md)
  Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [func endAppearanceTransition()](./endappearancetransition%28%29.md)
  Tells a child controller its appearance has changed.
- [class let hierarchyInconsistencyException: NSExceptionName](./hierarchyinconsistencyexception.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/beginappearancetransition(_:animated:))*