# hierarchyInconsistencyException

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Raised if the view controller hierarchy is inconsistent with the view hierarchy.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class let hierarchyInconsistencyException: NSExceptionName
```

```c
extern NSExceptionName const UIViewControllerHierarchyInconsistencyException;
```

#### Discussion

When a view controller’s view is added to the view hierarchy, the system walks up the view hierarchy to find the first parent view that has a view controller. That view controller must be the parent of the view controller whose view is being added. Otherwise, this exception is raised. This consistency check is also performed when a view controller is added as a child by calling the [`addChild(_:)`](./addchild%28_%29.md) method.

It is also allowed for a view controller that has no parent to add its view to the view hierarchy. This is generally not recommended, but is useful in some special cases.

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
- [func endAppearanceTransition()](./endappearancetransition%28%29.md)
  Tells a child controller its appearance has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/hierarchyinconsistencyexception)*