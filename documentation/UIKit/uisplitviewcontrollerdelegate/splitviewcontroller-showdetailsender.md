# splitViewController(_:showDetail:sender:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if it will do the work of displaying a view controller in the secondary position of the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewController(_ splitViewController: UISplitViewController, showDetail vc: UIViewController, sender: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you handled the presentation of the view controller, or [`false`](https://developer.apple.com/documentation/Swift/false) if you want the split view controller to do it.

#### Discussion

This delegate method only applies to classic split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

When its [`showDetailViewController(_:sender:)`](uisplitviewcontroller/showdetailviewcontroller(_:sender:).md) method is called, the split view controller calls this method to see if your delegate will handle the presentation of the specified view controller. If you implement this method and ultimately return [`true`](https://developer.apple.com/documentation/Swift/true), your implementation is responsible for presenting the specified view controller in the secondary position of the split view interface.

If you don’t implement this method or if your implementation returns [`false`](https://developer.apple.com/documentation/Swift/false), the split view controller presents the view controller.

## Parameters

- `splitViewController`: The split view controller whose secondary view controller is being updated.
- `vc`: The view controller being displayed in the secondary position.
- `sender`: The object that made the request.

## See Also

- [func splitViewController(UISplitViewController, show: UIViewController, sender: Any?) -> Bool](uisplitviewcontrollerdelegate/splitviewcontroller(_:show:sender:).md)
  Asks the delegate if it will do the work of displaying a view controller in the primary position of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:showdetail:sender:))*