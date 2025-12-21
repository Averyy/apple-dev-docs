# shouldAutomaticallyForwardAppearanceMethods

**Framework**: UIKit  
**Kind**: property

Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldAutomaticallyForwardAppearanceMethods: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if appearance methods are forwarded or [`false`](https://developer.apple.com/documentation/Swift/false) if they are not.

#### Discussion

This method is called to determine whether to automatically forward appearance-related containment callbacks to child view controllers.

The default implementation returns [`true`](https://developer.apple.com/documentation/Swift/true). Subclasses of the [`UIViewController`](uiviewcontroller.md) class that implement containment logic may override this method to control how these methods are forwarded. If you override this method and return [`false`](https://developer.apple.com/documentation/Swift/false), you are responsible for telling the child when its views are going to appear or disappear. You do this by calling the child view controller’s [`beginAppearanceTransition(_:animated:)`](uiviewcontroller/beginappearancetransition(_:animated:).md) and [`endAppearanceTransition()`](uiviewcontroller/endappearancetransition().md) methods.

## See Also

- [var children: [UIViewController]](uiviewcontroller/children.md)
  An array of view controllers that are children of the current view controller.
- [func addChild(UIViewController)](uiviewcontroller/addchild(_:).md)
  Adds the specified view controller as a child of the current view controller.
- [func removeFromParent()](uiviewcontroller/removefromparent.md)
  Removes the view controller from its parent.
- [func transition(from: UIViewController, to: UIViewController, duration: TimeInterval, options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiviewcontroller/transition(from:to:duration:options:animations:completion:).md)
  Transitions between two of the view controller’s child view controllers.
- [func beginAppearanceTransition(Bool, animated: Bool)](uiviewcontroller/beginappearancetransition(_:animated:).md)
  Tells a child controller its appearance is about to change.
- [func endAppearanceTransition()](uiviewcontroller/endappearancetransition.md)
  Tells a child controller its appearance has changed.
- [class let hierarchyInconsistencyException: NSExceptionName](uiviewcontroller/hierarchyinconsistencyexception.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldautomaticallyforwardappearancemethods)*