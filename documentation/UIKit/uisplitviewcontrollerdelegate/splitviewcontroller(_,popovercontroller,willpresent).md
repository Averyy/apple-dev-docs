# splitViewController(_:popoverController:willPresent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the hidden view controller is about to be displayed in a popover.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Orientation-related delegate methods are no longer supported.

## Declaration

```swift
optional func splitViewController(_ svc: UISplitViewController, popoverController pc: UIPopoverController, willPresent aViewController: UIViewController)
```

```objc
- (void) splitViewController:(UISplitViewController *) svc popoverController:(UIPopoverController *) pc willPresentViewController:(UIViewController *) aViewController;
```

## Discussion

The toolbar button you add to your user interface facilitates the display of the hidden view controller in response to user taps. When the user taps that button, the split view controller calls this method. You can use this method to perform any additional steps prior to displaying the currently hidden view controller.

## Parameters

- `svc`: The split view controller that owns the hidden view controller.
- `pc`: The popover controller that is about to display the view controller.
- `aViewController`: The view controller to be displayed in the popover.

## See Also

### Deprecated
- [func splitViewController(UISplitViewController, shouldHide: UIViewController, in: UIInterfaceOrientation) -> Bool](./splitviewcontroller%28_,shouldhide,in%29.md)
  Asks the delegate whether the first view controller should be hidden for the specified orientation.
- [func splitViewController(UISplitViewController, willHide: UIViewController, with: UIBarButtonItem, for: UIPopoverController)](./splitviewcontroller%28_,willhide,with,for%29.md)
  Tells the delegate that the specified view controller is about to be hidden.
- [func splitViewController(UISplitViewController, willShow: UIViewController, invalidating: UIBarButtonItem)](./splitviewcontroller%28_,willshow,invalidating%29.md)
  Tells the delegate that the specified view controller is about to be shown again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:popovercontroller:willpresent:))*