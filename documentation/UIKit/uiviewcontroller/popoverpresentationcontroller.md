# popoverPresentationController

**Framework**: UIKit  
**Kind**: property

The nearest popover presentation controller that is managing the current view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var popoverPresentationController: UIPopoverPresentationController? { get }
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Discussion

If the view controller or one of its ancestors is managed by a popover presentation controller, this property contains that object. This property is `nil` if the view controller is not managed by a popover presentation controller.

If you created the view controller but have not yet presented it, accessing this property creates a popover presentation controller when the value in the [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) property is [`UIModalPresentationStyle.popover`](uimodalpresentationstyle/popover.md). If the modal presentation style is a different value, this property is `nil`.

## See Also

- [var transitioningDelegate: (any UIViewControllerTransitioningDelegate)?](uiviewcontroller/transitioningdelegate.md)
  The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [var transitionCoordinator: (any UIViewControllerTransitionCoordinator)?](uiviewcontroller/transitioncoordinator.md)
  Returns the active transition coordinator object.
- [func targetViewController(forAction: Selector, sender: Any?) -> UIViewController?](uiviewcontroller/targetviewcontroller(foraction:sender:).md)
  Returns the view controller that responds to the action.
- [var presentationController: UIPresentationController?](uiviewcontroller/presentationcontroller.md)
  The presentation controller that’s managing the current view controller.
- [var sheetPresentationController: UISheetPresentationController?](uiviewcontroller/sheetpresentationcontroller.md)
  The sheet presentation controller for the view controller.
- [var activePresentationController: UIPresentationController?](uiviewcontroller/activepresentationcontroller.md)
  The presentation controller that’s managing the view controller.
- [var restoresFocusAfterTransition: Bool](uiviewcontroller/restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/popoverpresentationcontroller)*