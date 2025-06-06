# definesPresentationContext

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var definesPresentationContext: Bool { get set }
```

#### Discussion

When using the [`UIModalPresentationStyle.currentContext`](uimodalpresentationstyle/currentcontext.md) or [`UIModalPresentationStyle.overCurrentContext`](uimodalpresentationstyle/overcurrentcontext.md) style to present a view controller, this property controls which existing view controller in your view controller hierarchy is actually covered by the new content. When a context-based presentation occurs, UIKit starts at the presenting view controller and walks up the view controller hierarchy. If it finds a view controller whose value for this property is [`true`](https://developer.apple.com/documentation/swift/true), it asks that view controller to present the new view controller. If no view controller defines the presentation context, UIKit asks the window’s root view controller to handle the presentation.

The default value for this property is [`false`](https://developer.apple.com/documentation/swift/false). Some system-provided view controllers, such as [`UINavigationController`](uinavigationcontroller.md), change the default value to [`true`](https://developer.apple.com/documentation/swift/true).

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
- [var providesPresentationContextTransitionStyle: Bool](uiviewcontroller/providespresentationcontexttransitionstyle.md)
  A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [var disablesAutomaticKeyboardDismissal: Bool](uiviewcontroller/disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/definespresentationcontext)*