# targetViewController(forAction:sender:)

**Framework**: UIKit  
**Kind**: method

Returns the view controller that responds to the action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func targetViewController(forAction action: Selector, sender: Any?) -> UIViewController?
```

#### Return Value

The view controller that handles the specified action or `nil` if no view controller handles the action.

#### Discussion

This method returns the current view controller if that view controller overrides the method indicated by the `action` parameter. If the current view controller does not override that method, UIKit walks up the view hierarchy and returns the first view controller that does override it. If no view controller handles the action, this method returns `nil`.

A view controller can selectively respond to an action by returning an appropriate value from its [`canPerformAction(_:withSender:)`](uiresponder/canperformaction(_:withsender:).md) method.

## Parameters

- `action`: The requested action.
- `sender`: The object sending the request.

## See Also

- [var transitioningDelegate: (any UIViewControllerTransitioningDelegate)?](uiviewcontroller/transitioningdelegate.md)
  The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [var transitionCoordinator: (any UIViewControllerTransitionCoordinator)?](uiviewcontroller/transitioncoordinator.md)
  Returns the active transition coordinator object.
- [var presentationController: UIPresentationController?](uiviewcontroller/presentationcontroller.md)
  The presentation controller that’s managing the current view controller.
- [var popoverPresentationController: UIPopoverPresentationController?](uiviewcontroller/popoverpresentationcontroller.md)
  The nearest popover presentation controller that is managing the current view controller.
- [var sheetPresentationController: UISheetPresentationController?](uiviewcontroller/sheetpresentationcontroller.md)
  The sheet presentation controller for the view controller.
- [var activePresentationController: UIPresentationController?](uiviewcontroller/activepresentationcontroller.md)
  The presentation controller that’s managing the view controller.
- [var restoresFocusAfterTransition: Bool](uiviewcontroller/restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/targetviewcontroller(foraction:sender:))*