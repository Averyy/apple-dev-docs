# shouldAutomaticallyForwardAppearanceMethods

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var shouldAutomaticallyForwardAppearanceMethods: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL shouldAutomaticallyForwardAppearanceMethods;
```

## Return Value

[`true`](../../Swift/true.md) if appearance methods are forwarded or [`false`](../../Swift/false.md) if they are not.

## Discussion

This method is called to determine whether to automatically forward appearance-related containment callbacks to child view controllers.

The default implementation returns [`true`](../../Swift/true.md). Subclasses of the [`UIViewController`](../uiviewcontroller.md) class that implement containment logic may override this method to control how these methods are forwarded. If you override this method and return [`false`](../../Swift/false.md), you are responsible for telling the child when its views are going to appear or disappear. You do this by calling the child view controller’s [`beginAppearanceTransition(_:animated:)`](./beginappearancetransition%28_,animated%29.md) and [`endAppearanceTransition()`](./endappearancetransition%28%29.md) methods.

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
- [func beginAppearanceTransition(Bool, animated: Bool)](./beginappearancetransition%28_,animated%29.md)
  Tells a child controller its appearance is about to change.
- [func endAppearanceTransition()](./endappearancetransition%28%29.md)
  Tells a child controller its appearance has changed.
- [class let hierarchyInconsistencyException: NSExceptionName](./hierarchyinconsistencyexception.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldautomaticallyforwardappearancemethods)*