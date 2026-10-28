# restoresFocusAfterTransition

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var restoresFocusAfterTransition: Bool { get set }
```

```objc
@property (nonatomic) BOOL restoresFocusAfterTransition;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the item that was last focused automatically becomes focused when its view controller becomes visible and focusable. For example, if an item in the view controller is focused and a second view controller is presented, the original item becomes focused again when the second view controller is dismissed. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Adding a custom transition or presentation
- [var transitioningDelegate: (any UIViewControllerTransitioningDelegate)?](./transitioningdelegate.md)
  The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [var transitionCoordinator: (any UIViewControllerTransitionCoordinator)?](./transitioncoordinator.md)
  Returns the active transition coordinator object.
- [func targetViewController(forAction: Selector, sender: Any?) -> UIViewController?](./targetviewcontroller%28foraction,sender%29.md)
  Returns the view controller that responds to the action.
- [var presentationController: UIPresentationController?](./presentationcontroller.md)
  The presentation controller that’s managing the current view controller.
- [var popoverPresentationController: UIPopoverPresentationController?](./popoverpresentationcontroller.md)
  The nearest popover presentation controller that is managing the current view controller.
- [var sheetPresentationController: UISheetPresentationController?](./sheetpresentationcontroller.md)
  The sheet presentation controller for the view controller.
- [var activePresentationController: UIPresentationController?](./activepresentationcontroller.md)
  The presentation controller that’s managing the view controller.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/restoresfocusaftertransition)*