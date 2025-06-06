# activePresentationController

**Framework**: UIKit  
**Kind**: property

The presentation controller that’s managing the view controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var activePresentationController: UIPresentationController? { get }
```

#### Discussion

If the original presentation controller hasn’t adapted, the value of this property is [`presentationController`](uiviewcontroller/presentationcontroller.md). If the original presentation controller has adapted to a different presentation controller, the value of this property is the adaptive presentation controller.

If the view controller hasn’t presented yet, this property returns `nil`.

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
- [var sheetPresentationController: UISheetPresentationController?](uiviewcontroller/sheetpresentationcontroller.md)
  The sheet presentation controller for the view controller.
- [var restoresFocusAfterTransition: Bool](uiviewcontroller/restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/activepresentationcontroller)*