# disablesAutomaticKeyboardDismissal

**Framework**: UIKit  
**Kind**: property

Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var disablesAutomaticKeyboardDismissal: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to prevent the dismissal of the input view or [`false`](https://developer.apple.com/documentation/swift/false) if the input view may be dismissed.

#### Discussion

Override this method in a subclass to allow or disallow the dismissal of the current input view (usually the system keyboard) when changing from a control that wants the input view to one that does not. Under normal circumstances, when the user taps a control that requires an input view, the system automatically displays that view. Tapping in a control that does not want an input view subsequently causes the current input view to be dismissed but may not in all cases. You can override this method in those outstanding cases to allow the input view to be dismissed or use this method to prevent the view from being dismissed in other cases.

The default implementation of this method returns [`true`](https://developer.apple.com/documentation/swift/true) when the modal presentation style of the view controller is set to [`UIModalPresentationStyle.formSheet`](uimodalpresentationstyle/formsheet.md) and returns [`false`](https://developer.apple.com/documentation/swift/false) for other presentation styles. Thus, the system normally does not allow the keyboard to be dismissed for modal forms.

## See Also

- [func show(UIViewController, sender: Any?)](uiviewcontroller/show(_:sender:).md)
  Presents a view controller in a primary context.
- [func showDetailViewController(UIViewController, sender: Any?)](uiviewcontroller/showdetailviewcontroller(_:sender:).md)
  Presents a view controller in a secondary (or detail) context.
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
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/disablesautomatickeyboarddismissal)*