# splitViewController(_:popoverController:willPresent:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the hidden view controller is about to be displayed in a popover.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, popoverController pc: UIPopoverController, willPresent aViewController: UIViewController)
```

#### Discussion

The toolbar button you add to your user interface facilitates the display of the hidden view controller in response to user taps. When the user taps that button, the split view controller calls this method. You can use this method to perform any additional steps prior to displaying the currently hidden view controller.

## Parameters

- `svc`: The split view controller that owns the hidden view controller.
- `pc`: The popover controller that is about to display the view controller.
- `aViewController`: The view controller to be displayed in the popover.

## See Also

- [func splitViewController(UISplitViewController, shouldHide: UIViewController, in: UIInterfaceOrientation) -> Bool](uisplitviewcontrollerdelegate/splitviewcontroller(_:shouldhide:in:).md)
  Asks the delegate whether the first view controller should be hidden for the specified orientation.
- [func splitViewController(UISplitViewController, willHide: UIViewController, with: UIBarButtonItem, for: UIPopoverController)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:with:for:).md)
  Tells the delegate that the specified view controller is about to be hidden.
- [func splitViewController(UISplitViewController, willShow: UIViewController, invalidating: UIBarButtonItem)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:invalidating:).md)
  Tells the delegate that the specified view controller is about to be shown again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:popovercontroller:willpresent:))*