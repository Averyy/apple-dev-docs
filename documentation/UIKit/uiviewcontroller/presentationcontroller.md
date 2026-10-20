# presentationController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The presentation controller that’s managing the current view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var presentationController: UIPresentationController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIPresentationController * presentationController;
```

#### Discussion

If the view controller is managed by a presentation controller, this property contains that object. This property is `nil` if the view controller isn’t managed by a presentation controller.

If you’ve not yet presented the current view controller, accessing this property creates a presentation controller based on the current value in the [`modalPresentationStyle`](./modalpresentationstyle.md) property. Always set the value of that property before accessing any presentation controllers.

## See Also

### Adding a custom transition or presentation
- [var transitioningDelegate: (any UIViewControllerTransitioningDelegate)?](./transitioningdelegate.md)
  The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [var transitionCoordinator: (any UIViewControllerTransitionCoordinator)?](./transitioncoordinator.md)
  Returns the active transition coordinator object.
- [func targetViewController(forAction: Selector, sender: Any?) -> UIViewController?](./targetviewcontroller%28foraction,sender%29.md)
  Returns the view controller that responds to the action.
- [var popoverPresentationController: UIPopoverPresentationController?](./popoverpresentationcontroller.md)
  The nearest popover presentation controller that is managing the current view controller.
- [var sheetPresentationController: UISheetPresentationController?](./sheetpresentationcontroller.md)
  The sheet presentation controller for the view controller.
- [var activePresentationController: UIPresentationController?](./activepresentationcontroller.md)
  The presentation controller that’s managing the view controller.
- [var restoresFocusAfterTransition: Bool](./restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/presentationcontroller)*