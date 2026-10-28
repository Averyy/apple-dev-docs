# activePresentationController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The presentation controller that’s managing the view controller.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var activePresentationController: UIPresentationController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIPresentationController * activePresentationController;
```

## Discussion

If the original presentation controller hasn’t adapted, the value of this property is [`presentationController`](./presentationcontroller.md). If the original presentation controller has adapted to a different presentation controller, the value of this property is the adaptive presentation controller.

If the view controller hasn’t presented yet, this property returns `nil`.

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
- [var restoresFocusAfterTransition: Bool](./restoresfocusaftertransition.md)
  A Boolean value that indicates whether an item that previously was focused should again become focused when the item’s view controller becomes visible and focusable.
- [Customizing and resizing sheets in UIKit](../customizing-and-resizing-sheets-in-uikit.md)
  Discover how to create a layered and customized sheet experience in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/activepresentationcontroller)*