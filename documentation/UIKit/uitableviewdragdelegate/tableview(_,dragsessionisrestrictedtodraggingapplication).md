# tableView(_:dragSessionIsRestrictedToDraggingApplication:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the dragged content must be dropped in the same app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, dragSessionIsRestrictedToDraggingApplication session: any UIDragSession) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView dragSessionIsRestrictedToDraggingApplication:(id<UIDragSession>) session;
```

## Return Value

[`true`](../../Swift/true.md) if the dragged content must be dropped in the same app that originated the drag, or [`false`](../../Swift/false.md) if the content may be dragged to other apps.

## Discussion

Implement this method when you want to allow the user to drag content within your app, but prevent them from dragging that same content to other apps. If you don’t implement this method, the table view behaves as if the method returned [`false`](../../Swift/false.md).

## Parameters

- `tableView`: The table view from which the drag operation originated.
- `session`: The drag session object containing information about the drag operation.

## See Also

### Tracking the drag session
- [func tableView(UITableView, dragSessionWillBegin: any UIDragSession)](./tableview%28_,dragsessionwillbegin%29.md)
  Signals the start of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionDidEnd: any UIDragSession)](./tableview%28_,dragsessiondidend%29.md)
  Signals the end of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionAllowsMoveOperation: any UIDragSession) -> Bool](./tableview%28_,dragsessionallowsmoveoperation%29.md)
  Returns a Boolean value indicating whether your app supports a move operation for the dragged content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionisrestrictedtodraggingapplication:))*