# popoverPresentationController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The nearest popover presentation controller that is managing the current view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var popoverPresentationController: UIPopoverPresentationController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIPopoverPresentationController * popoverPresentationController;
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](../getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Discussion

If the view controller or one of its ancestors is managed by a popover presentation controller, this property contains that object. This property is `nil` if the view controller is not managed by a popover presentation controller.

If you created the view controller but have not yet presented it, accessing this property creates a popover presentation controller when the value in the [`modalPresentationStyle`](./modalpresentationstyle.md) property is [`UIModalPresentationStyle.popover`](../uimodalpresentationstyle/popover.md). If the modal presentation style is a different value, this property is `nil`.

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
- [var sheetPresentationController: UISheetPresentationController?](./sheetpresentationcontroller.md)
  The sheet presentation controller for the view controller.
- [var activePresentationController: UIPresentationController?](./activepresentationcontroller.md)
  The presentation controller that’s managing the view controller.
- [var restoresFocusAfterTransition: Bool](./restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/popoverpresentationcontroller)*