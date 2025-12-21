# splitViewController(_:shouldHide:in:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the first view controller should be hidden for the specified orientation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func splitViewController(_ svc: UISplitViewController, shouldHide vc: UIViewController, in orientation: UIInterfaceOrientation) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the view controller should be hidden in the specified orientation or [`false`](https://developer.apple.com/documentation/Swift/false) if it should be visible. If you do not implement this method, a value of [`true`](https://developer.apple.com/documentation/Swift/true) is assumed for portrait orientations and [`false`](https://developer.apple.com/documentation/Swift/false) is assumed for landscape orientations.

#### Discussion

The split view controller calls this method only for the first child view controller in its array. The second view controller always remains visible regardless of the orientation.

Prior to iOS 5.0, the first view controller was always hidden in portrait orientations and always shown in landscape orientations. If you do not implement this method in your delegate object, that default behavior remains in effect.

## Parameters

- `svc`: The split view controller that owns the first view controller.
- `vc`: The first view controller in the array of view controllers.
- `orientation`: The orientation being considered.

## See Also

- [func splitViewController(UISplitViewController, willHide: UIViewController, with: UIBarButtonItem, for: UIPopoverController)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:with:for:).md)
  Tells the delegate that the specified view controller is about to be hidden.
- [func splitViewController(UISplitViewController, willShow: UIViewController, invalidating: UIBarButtonItem)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:invalidating:).md)
  Tells the delegate that the specified view controller is about to be shown again.
- [func splitViewController(UISplitViewController, popoverController: UIPopoverController, willPresent: UIViewController)](uisplitviewcontrollerdelegate/splitviewcontroller(_:popovercontroller:willpresent:).md)
  Tells the delegate that the hidden view controller is about to be displayed in a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:shouldhide:in:))*