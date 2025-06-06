# splitViewController(_:willShow:invalidating:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified view controller is about to be shown again.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, willShow aViewController: UIViewController, invalidating barButtonItem: UIBarButtonItem)
```

#### Discussion

When the view controller rotates from a portrait to landscape orientation, it shows its hidden view controller once more. If you added the specified button to your toolbar to facilitate the display of the hidden view controller in a popover, you must implement this method and use it to remove that button.

## Parameters

- `svc`: The split view controller that owns the specified view controller.
- `aViewController`: The view controller being hidden.
- `barButtonItem`: The button used to display the view controller while it was hidden.

## See Also

- [func splitViewController(UISplitViewController, shouldHide: UIViewController, in: UIInterfaceOrientation) -> Bool](uisplitviewcontrollerdelegate/splitviewcontroller(_:shouldhide:in:).md)
  Asks the delegate whether the first view controller should be hidden for the specified orientation.
- [func splitViewController(UISplitViewController, willHide: UIViewController, with: UIBarButtonItem, for: UIPopoverController)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:with:for:).md)
  Tells the delegate that the specified view controller is about to be hidden.
- [func splitViewController(UISplitViewController, popoverController: UIPopoverController, willPresent: UIViewController)](uisplitviewcontrollerdelegate/splitviewcontroller(_:popovercontroller:willpresent:).md)
  Tells the delegate that the hidden view controller is about to be displayed in a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:invalidating:))*