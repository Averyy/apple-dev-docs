# endAppearanceTransition()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells a child controller its appearance has changed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func endAppearanceTransition()
```

```objc
- (void) endAppearanceTransition;
```

## Discussion

If you are implementing a custom container controller, use this method to tell the child that the view transition is complete.

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
- [func beginAppearanceTransition(Bool, animated: Bool)](./beginappearancetransition%28_,animated%29.md)
  Tells a child controller its appearance is about to change.
- [class let hierarchyInconsistencyException: NSExceptionName](./hierarchyinconsistencyexception.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/endappearancetransition())*