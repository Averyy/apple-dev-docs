# splitViewController(_:willHide:with:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified view controller is about to be hidden.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Implement the [`splitViewController(_:willChangeTo:)`](./splitviewcontroller%28_,willchangeto%29.md) method instead.

## Declaration

```swift
optional func splitViewController(_ svc: UISplitViewController, willHide aViewController: UIViewController, with barButtonItem: UIBarButtonItem, for pc: UIPopoverController)
```

```objc
- (void) splitViewController:(UISplitViewController *) svc willHideViewController:(UIViewController *) aViewController withBarButtonItem:(UIBarButtonItem *) barButtonItem forPopoverController:(UIPopoverController *) pc;
```

#### Discussion

When the split view controller rotates from a landscape to portrait orientation, it typically hides one of its view controllers. When that happens, it calls this method to coordinate the addition of a button to the toolbar (or navigation bar) of the remaining custom view controller. If you want the soon-to-be hidden view controller to be displayed in a popover, you must implement this method and use it to add the specified button to your interface.

## Parameters

- `svc`: The split view controller that owns the specified view controller.
- `aViewController`: The view controller being hidden.
- `barButtonItem`: A button you can add to your toolbar.
- `pc`: The popover controller that uses taps in `barButtonItem` to display the specified view controller.

## See Also

### Deprecated
- [func splitViewController(UISplitViewController, shouldHide: UIViewController, in: UIInterfaceOrientation) -> Bool](./splitviewcontroller%28_,shouldhide,in%29.md)
  Asks the delegate whether the first view controller should be hidden for the specified orientation.
- [func splitViewController(UISplitViewController, willShow: UIViewController, invalidating: UIBarButtonItem)](./splitviewcontroller%28_,willshow,invalidating%29.md)
  Tells the delegate that the specified view controller is about to be shown again.
- [func splitViewController(UISplitViewController, popoverController: UIPopoverController, willPresent: UIViewController)](./splitviewcontroller%28_,popovercontroller,willpresent%29.md)
  Tells the delegate that the hidden view controller is about to be displayed in a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:with:for:))*