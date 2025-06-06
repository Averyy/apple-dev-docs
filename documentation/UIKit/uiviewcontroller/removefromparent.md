# removeFromParent()

**Framework**: UIKit  
**Kind**: method

Removes the view controller from its parent.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeFromParent()
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)

#### Discussion

This method is only intended to be called by an implementation of a custom container view controller. If you override this method, you must call `super` in your implementation.

## See Also

- [var children: [UIViewController]](uiviewcontroller/children.md)
  An array of view controllers that are children of the current view controller.
- [func addChild(UIViewController)](uiviewcontroller/addchild(_:).md)
  Adds the specified view controller as a child of the current view controller.
- [func transition(from: UIViewController, to: UIViewController, duration: TimeInterval, options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiviewcontroller/transition(from:to:duration:options:animations:completion:).md)
  Transitions between two of the view controller’s child view controllers.
- [var shouldAutomaticallyForwardAppearanceMethods: Bool](uiviewcontroller/shouldautomaticallyforwardappearancemethods.md)
  Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [func beginAppearanceTransition(Bool, animated: Bool)](uiviewcontroller/beginappearancetransition(_:animated:).md)
  Tells a child controller its appearance is about to change.
- [func endAppearanceTransition()](uiviewcontroller/endappearancetransition.md)
  Tells a child controller its appearance has changed.
- [class let hierarchyInconsistencyException: NSExceptionName](uiviewcontroller/hierarchyinconsistencyexception.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/removefromparent())*