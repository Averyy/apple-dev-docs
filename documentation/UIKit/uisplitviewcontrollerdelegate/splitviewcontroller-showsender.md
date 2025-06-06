# splitViewController(_:show:sender:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if it will do the work of displaying a view controller in the primary position of the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewController(_ splitViewController: UISplitViewController, show vc: UIViewController, sender: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you handled the presentation of the view controller, or [`false`](https://developer.apple.com/documentation/swift/false) if you want the split view controller to do it.

#### Discussion

This delegate method only applies to classic split view interfaces. For more information, see [`Split view styles`](uisplitviewcontroller#Split-view-styles.md).

When its [`show(_:sender:)`](uisplitviewcontroller/show(_:sender:).md) method is called, the split view controller calls this method to see if your delegate will handle the presentation of the specified view controller. If you implement this method and your implementation returns [`true`](https://developer.apple.com/documentation/swift/true), you are responsible for presenting the specified view controller in the primary position of the split view interface. The split view controller does nothing more to try to show the view controller.

If you don’t implement this method or if your implementation returns [`false`](https://developer.apple.com/documentation/swift/false), the split view controller presents the view controller.

## Parameters

- `splitViewController`: The split view controller whose primary view controller is being updated.
- `vc`: The view controller being displayed in the primary position.
- `sender`: The object that made the request.

## See Also

- [func splitViewController(UISplitViewController, showDetail: UIViewController, sender: Any?) -> Bool](uisplitviewcontrollerdelegate/splitviewcontroller(_:showdetail:sender:).md)
  Asks the delegate if it will do the work of displaying a view controller in the secondary position of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:show:sender:))*