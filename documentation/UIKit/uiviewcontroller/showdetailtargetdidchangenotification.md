# showDetailTargetDidChangeNotification

**Framework**: UIKit  
**Kind**: property

Posted when a split view controller is expanded or collapsed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let showDetailTargetDidChangeNotification: NSNotification.Name
```

#### Discussion

When a view controller is using [`show(_:sender:)`](uiviewcontroller/show(_:sender:).md) or [`showDetailViewController(_:sender:)`](uiviewcontroller/showdetailviewcontroller(_:sender:).md), it may need to know when a split view controller higher in the view hierarchy has changed. This notification is sent when a split view controller expands or collapses. The object of this notification is the view controller that caused the change.

## See Also

- [func show(UIViewController, sender: Any?)](uiviewcontroller/show(_:sender:).md)
  Presents a view controller in a primary context.
- [func showDetailViewController(UIViewController, sender: Any?)](uiviewcontroller/showdetailviewcontroller(_:sender:).md)
  Presents a view controller in a secondary (or detail) context.
- [UIViewController.ShowDetailTargetDidChangeMessage](uiviewcontroller/showdetailtargetdidchangemessage.md)
- [func present(UIViewController, animated: Bool, completion: (() -> Void)?)](uiviewcontroller/present(_:animated:completion:).md)
  Presents a view controller modally.
- [func dismiss(animated: Bool, completion: (() -> Void)?)](uiviewcontroller/dismiss(animated:completion:).md)
  Dismisses the view controller that was presented modally by the view controller.
- [var modalPresentationStyle: UIModalPresentationStyle](uiviewcontroller/modalpresentationstyle.md)
  The presentation style for modal view controllers.
- [enum UIModalPresentationStyle](uimodalpresentationstyle.md)
  Modal presentation styles available when presenting view controllers.
- [var modalTransitionStyle: UIModalTransitionStyle](uiviewcontroller/modaltransitionstyle.md)
  The transition style to use when presenting the view controller.
- [enum UIModalTransitionStyle](uimodaltransitionstyle.md)
  Transition styles available when presenting view controllers.
- [var isModalInPresentation: Bool](uiviewcontroller/ismodalinpresentation.md)
  A Boolean value indicating whether the view controller enforces a modal behavior.
- [var definesPresentationContext: Bool](uiviewcontroller/definespresentationcontext.md)
  A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [var providesPresentationContextTransitionStyle: Bool](uiviewcontroller/providespresentationcontexttransitionstyle.md)
  A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [var disablesAutomaticKeyboardDismissal: Bool](uiviewcontroller/disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/showdetailtargetdidchangenotification)*