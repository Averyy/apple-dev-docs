# show(_:sender:)

**Framework**: UIKit  
**Kind**: method

Presents a view controller in a primary context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func show(_ vc: UIViewController, sender: Any?)
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)
- [Customizing the behavior of segue-based presentations](customizing-the-behavior-of-segue-based-presentations.md)

#### Discussion

You use this method to decouple the need to display a view controller from the process of actually presenting that view controller onscreen. Using this method, a view controller does not need to know whether it is embedded inside a navigation controller or split-view controller. It calls the same method for both. The [`UISplitViewController`](uisplitviewcontroller.md) and [`UINavigationController`](uinavigationcontroller.md) classes override this method and handle the presentation according to their design. For example, a navigation controller overrides this method and uses it to push `vc` onto its navigation stack.

The default implementation of this method calls the [`targetViewController(forAction:sender:)`](uiviewcontroller/targetviewcontroller(foraction:sender:).md) method to locate an object in the view controller hierarchy that overrides this method. It then calls the method on that target object, which displays the view controller in an appropriate way. If the [`targetViewController(forAction:sender:)`](uiviewcontroller/targetviewcontroller(foraction:sender:).md) method returns `nil`, this method uses the window’s root view controller to present `vc` modally.

You can override this method in custom view controllers to display `vc` yourself. Use this method to display `vc` in a primary context. For example, a container view controller might use this method to replace its primary child. Your implementation should adapt its behavior for both regular and compact environments.

## Parameters

- `vc`: The view controller to display.
- `sender`: The object that initiated the request.

## See Also

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
- [var disablesAutomaticKeyboardDismissal: Bool](uiviewcontroller/disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/show(_:sender:))*