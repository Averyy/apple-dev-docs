# showDetailTargetDidChangeNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Posted when a split view controller is expanded or collapsed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let showDetailTargetDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIViewControllerShowDetailTargetDidChangeNotification;
```

## Discussion

When a view controller is using [`show(_:sender:)`](./show%28_,sender%29.md) or [`showDetailViewController(_:sender:)`](./showdetailviewcontroller%28_,sender%29.md), it may need to know when a split view controller higher in the view hierarchy has changed. This notification is sent when a split view controller expands or collapses. The object of this notification is the view controller that caused the change.

## See Also

### Presenting a view controller
- [func show(UIViewController, sender: Any?)](./show%28_,sender%29.md)
  Presents a view controller in a primary context.
- [func showDetailViewController(UIViewController, sender: Any?)](./showdetailviewcontroller%28_,sender%29.md)
  Presents a view controller in a secondary (or detail) context.
- [UIViewController.ShowDetailTargetDidChangeMessage](./showdetailtargetdidchangemessage.md)
- [func present(UIViewController, animated: Bool, completion: (() -> Void)?)](./present%28_,animated,completion%29.md)
  Presents a view controller modally.
- [func dismiss(animated: Bool, completion: (() -> Void)?)](./dismiss%28animated,completion%29.md)
  Dismisses the view controller that was presented modally by the view controller.
- [var modalPresentationStyle: UIModalPresentationStyle](./modalpresentationstyle.md)
  The presentation style for modal view controllers.
- [enum UIModalPresentationStyle](../uimodalpresentationstyle.md)
  Modal presentation styles available when presenting view controllers.
- [var modalTransitionStyle: UIModalTransitionStyle](./modaltransitionstyle.md)
  The transition style to use when presenting the view controller.
- [enum UIModalTransitionStyle](../uimodaltransitionstyle.md)
  Transition styles available when presenting view controllers.
- [var isModalInPresentation: Bool](./ismodalinpresentation.md)
  A Boolean value indicating whether the view controller enforces a modal behavior.
- [var definesPresentationContext: Bool](./definespresentationcontext.md)
  A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [var providesPresentationContextTransitionStyle: Bool](./providespresentationcontexttransitionstyle.md)
  A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [var disablesAutomaticKeyboardDismissal: Bool](./disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/showdetailtargetdidchangenotification)*