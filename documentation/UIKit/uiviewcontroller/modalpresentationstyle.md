# modalPresentationStyle

**Framework**: UIKit  
**Kind**: property

The presentation style for modal view controllers.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var modalPresentationStyle: UIModalPresentationStyle { get set }
```

#### Discussion

Presentation style defines how the system presents a modal view controller. The system uses this value only in regular-width size classes. In compact-width size classes, some styles take on the behavior of other styles. You can influence this behavior by implementing the [`adaptivePresentationStyle(for:traitCollection:)`](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:traitcollection:).md) method.

Presentation style also impacts the content size of a modal view controller. For example, [`UIModalPresentationStyle.pageSheet`](uimodalpresentationstyle/pagesheet.md) uses an explicit size that the system provides. By contrast, [`UIModalPresentationStyle.formSheet`](uimodalpresentationstyle/formsheet.md) uses the view controller’s [`preferredContentSize`](uiviewcontroller/preferredcontentsize.md) property, which you can set.

The default value is [`UIModalPresentationStyle.automatic`](uimodalpresentationstyle/automatic.md). For a list of presentation styles and their compatibility with the various transition styles, see [`UIModalPresentationStyle`](uimodalpresentationstyle.md).

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
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/modalpresentationstyle)*