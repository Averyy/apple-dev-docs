# transitioningDelegate

**Framework**: UIKit  
**Kind**: property

The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var transitioningDelegate: (any UIViewControllerTransitioningDelegate)? { get set }
```

#### Discussion

When the view controller’s [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) property is [`UIModalPresentationStyle.custom`](uimodalpresentationstyle/custom.md), UIKit uses the object in this property to facilitate transitions and presentations for the view controller. The transitioning delegate object is a custom object that you provide and that conforms to the [`UIViewControllerTransitioningDelegate`](uiviewcontrollertransitioningdelegate.md) protocol. Its job is to vend the animator objects used to animate this view controller’s view onscreen and an optional presentation controller to provide any additional chrome and animations.

## See Also

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
- [var activePresentationController: UIPresentationController?](uiviewcontroller/activepresentationcontroller.md)
  The presentation controller that’s managing the view controller.
- [var restoresFocusAfterTransition: Bool](uiviewcontroller/restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transitioningdelegate)*