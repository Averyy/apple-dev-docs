# beginAppearanceTransition(_:animated:)

**Framework**: UIKit  
**Kind**: method

Tells a child controller its appearance is about to change.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func beginAppearanceTransition(_ isAppearing: Bool, animated: Bool)
```

#### Discussion

If you are implementing a custom container controller, use this method to tell the child that its views are about to appear or disappear. Do not invoke [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md), [`viewWillDisappear(_:)`](uiviewcontroller/viewwilldisappear(_:).md), [`viewDidAppear(_:)`](uiviewcontroller/viewdidappear(_:).md), or [`viewDidDisappear(_:)`](uiviewcontroller/viewdiddisappear(_:).md) directly.

## Parameters

- `isAppearing`:   if the child view controller’s view is about to be added to the view hierarchy,   if it is being removed.
- `animated`: If  , the transition is being animated.

## See Also

- [var children: [UIViewController]](uiviewcontroller/children.md)
  An array of view controllers that are children of the current view controller.
- [func addChild(UIViewController)](uiviewcontroller/addchild(_:).md)
  Adds the specified view controller as a child of the current view controller.
- [func removeFromParent()](uiviewcontroller/removefromparent.md)
  Removes the view controller from its parent.
- [func transition(from: UIViewController, to: UIViewController, duration: TimeInterval, options: UIView.AnimationOptions, animations: (() -> Void)?, completion: ((Bool) -> Void)?)](uiviewcontroller/transition(from:to:duration:options:animations:completion:).md)
  Transitions between two of the view controller’s child view controllers.
- [var shouldAutomaticallyForwardAppearanceMethods: Bool](uiviewcontroller/shouldautomaticallyforwardappearancemethods.md)
  Returns a Boolean value indicating whether appearance methods are forwarded to child view controllers.
- [func endAppearanceTransition()](uiviewcontroller/endappearancetransition.md)
  Tells a child controller its appearance has changed.
- [class let hierarchyInconsistencyException: NSExceptionName](uiviewcontroller/hierarchyinconsistencyexception.md)
  Raised if the view controller hierarchy is inconsistent with the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/beginappearancetransition(_:animated:))*