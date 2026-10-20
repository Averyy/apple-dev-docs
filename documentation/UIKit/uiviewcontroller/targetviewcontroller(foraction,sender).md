# targetViewController(forAction:sender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the view controller that responds to the action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func targetViewController(forAction action: Selector, sender: Any?) -> UIViewController?
```

```objc
- (UIViewController *) targetViewControllerForAction:(SEL) action sender:(id) sender;
```

#### Return Value

The view controller that handles the specified action or `nil` if no view controller handles the action.

#### Discussion

This method returns the current view controller if that view controller overrides the method indicated by the `action` parameter. If the current view controller does not override that method, UIKit walks up the view hierarchy and returns the first view controller that does override it. If no view controller handles the action, this method returns `nil`.

A view controller can selectively respond to an action by returning an appropriate value from its [`canPerformAction(_:withSender:)`](../uiresponder/canperformaction%28_,withsender%29.md) method.

## Parameters

- `action`: The requested action.
- `sender`: The object sending the request.

## See Also

### Adding a custom transition or presentation
- [var transitioningDelegate: (any UIViewControllerTransitioningDelegate)?](./transitioningdelegate.md)
  The delegate object that provides transition animator, interactive controller, and custom presentation controller objects.
- [var transitionCoordinator: (any UIViewControllerTransitionCoordinator)?](./transitioncoordinator.md)
  Returns the active transition coordinator object.
- [var presentationController: UIPresentationController?](./presentationcontroller.md)
  The presentation controller that’s managing the current view controller.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/targetviewcontroller(foraction:sender:))*