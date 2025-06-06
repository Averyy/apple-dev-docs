# sheetPresentationController

**Framework**: UIKit  
**Kind**: property

The sheet presentation controller for the view controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sheetPresentationController: UISheetPresentationController? { get }
```

#### Discussion

If [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) is [`UIModalPresentationStyle.pageSheet`](uimodalpresentationstyle/pagesheet.md) or [`UIModalPresentationStyle.formSheet`](uimodalpresentationstyle/formsheet.md), this property contains a sheet presentation controller instance. Access this instance to customize or adjust the sheet before or after it presents.

If [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) has a value other than [`UIModalPresentationStyle.pageSheet`](uimodalpresentationstyle/pagesheet.md) or [`UIModalPresentationStyle.formSheet`](uimodalpresentationstyle/formsheet.md), the value of this property is `nil`.

## See Also

- [var transitioningDelegate: (any UIViewControllerTransitioningDelegate)?](uiviewcontroller/transitioningdelegate.md)
  The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [var transitionCoordinator: (any UIViewControllerTransitionCoordinator)?](uiviewcontroller/transitioncoordinator.md)
  Returns the active transition coordinator object.
- [func targetViewController(forAction: Selector, sender: Any?) -> UIViewController?](uiviewcontroller/targetviewcontroller(foraction:sender:).md)
  Returns the view controller that responds to the action.
- [var presentationController: UIPresentationController?](uiviewcontroller/presentationcontroller.md)
  The presentation controller that’s managing the current view controller.
- [var popoverPresentationController: UIPopoverPresentationController?](uiviewcontroller/popoverpresentationcontroller.md)
  The nearest popover presentation controller that is managing the current view controller.
- [var activePresentationController: UIPresentationController?](uiviewcontroller/activepresentationcontroller.md)
  The presentation controller that’s managing the view controller.
- [var restoresFocusAfterTransition: Bool](uiviewcontroller/restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/sheetpresentationcontroller)*