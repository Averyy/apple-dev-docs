# present(_:animated:completion:)

**Framework**: UIKit  
**Kind**: method

Presents a view controller modally.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func present(_ viewControllerToPresent: UIViewController, animated flag: Bool, completion: (() -> Void)? = nil)
```

## Mentions

- [Presenting selected documents](presenting-selected-documents.md)
- [Displaying transient content in a popover](displaying-transient-content-in-a-popover.md)
- [Providing access to directories](providing-access-to-directories.md)
- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Discussion

In a horizontally regular environment, the view controller is presented in the style specified by the [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) property. In a horizontally compact environment, the view controller is presented full screen by default. If you associate an adaptive delegate with the presentation controller associated with the object in `viewControllerToPresent`, you can modify the presentation style dynamically.

The object on which you call this method may not always be the one that handles the presentation. Each presentation style has different rules governing its behavior. For example, a full-screen presentation must be made by a view controller that itself covers the entire screen. If the current view controller is unable to fulfill a request, it forwards the request up the view controller hierarchy to its nearest parent, which can then handle or forward the request.

Before displaying the view controller, this method resizes the presented view controller’s view based on the presentation style. For most presentation styles, the resulting view is then animated onscreen using the transition style in the [`modalTransitionStyle`](uiviewcontroller/modaltransitionstyle.md) property of the presented view controller. For custom presentations, the view is animated onscreen using the presented view controller’s transitioning delegate. For current context presentations, the view may be animated onscreen using the current view controller’s transition style.

The completion handler is called after the [`viewDidAppear(_:)`](uiviewcontroller/viewdidappear(_:).md) method is called on the presented view controller.

## Parameters

- `viewControllerToPresent`: The view controller to display over the current view controller’s content.
- `flag`: Pass   to animate the presentation; otherwise, pass  .
- `completion`: The block to execute after the presentation finishes. This block has no return value and takes no parameters. You may specify   for this parameter.

## See Also

- [var presentedViewController: UIViewController?](uiviewcontroller/presentedviewcontroller.md)
  The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [var presentingViewController: UIViewController?](uiviewcontroller/presentingviewcontroller.md)
  The view controller that presented this view controller.
- [func show(UIViewController, sender: Any?)](uiviewcontroller/show(_:sender:).md)
  Presents a view controller in a primary context.
- [func showDetailViewController(UIViewController, sender: Any?)](uiviewcontroller/showdetailviewcontroller(_:sender:).md)
  Presents a view controller in a secondary (or detail) context.
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
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/present(_:animated:completion:))*