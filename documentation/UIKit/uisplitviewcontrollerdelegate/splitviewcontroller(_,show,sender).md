# splitViewController(_:show:sender:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if it will do the work of displaying a view controller in the primary position of the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func splitViewController(_ splitViewController: UISplitViewController, show vc: UIViewController, sender: Any?) -> Bool
```

```objc
- (BOOL) splitViewController:(UISplitViewController *) splitViewController showViewController:(UIViewController *) vc sender:(id) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if you handled the presentation of the view controller, or [`false`](../../Swift/false.md) if you want the split view controller to do it.

#### Discussion

This delegate method only applies to classic split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

When its [`show(_:sender:)`](../uisplitviewcontroller/show%28_,sender%29.md) method is called, the split view controller calls this method to see if your delegate will handle the presentation of the specified view controller. If you implement this method and your implementation returns [`true`](../../Swift/true.md), you are responsible for presenting the specified view controller in the primary position of the split view interface. The split view controller does nothing more to try to show the view controller.

If you don’t implement this method or if your implementation returns [`false`](../../Swift/false.md), the split view controller presents the view controller.

## Parameters

- `splitViewController`: The split view controller whose primary view controller is being updated.
- `vc`: The view controller being displayed in the primary position.
- `sender`: The object that made the request.

## See Also

### Overriding the presentation behavior
- [func splitViewController(UISplitViewController, showDetail: UIViewController, sender: Any?) -> Bool](./splitviewcontroller%28_,showdetail,sender%29.md)
  Asks the delegate if it will do the work of displaying a view controller in the secondary position of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:show:sender:))*