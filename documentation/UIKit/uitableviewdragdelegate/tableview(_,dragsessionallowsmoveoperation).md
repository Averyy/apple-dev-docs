# tableView(_:dragSessionAllowsMoveOperation:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether your app supports a move operation for the dragged content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, dragSessionAllowsMoveOperation session: any UIDragSession) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView dragSessionAllowsMoveOperation:(id<UIDragSession>) session;
```

## Return Value

[`true`](../../Swift/true.md) if your app allows content to be moved instead of copied, or [`false`](../../Swift/false.md) if moves are not supported.

## Discussion

Implement this method if you want to prevent the dragged content from being moved. If your delegate returns [`false`](../../Swift/false.md) and the drop operation type is [`UIDropOperation.move`](../uidropoperation/move.md), the system cancels the drop.

If you don’t implement this method, the table view behaves as if the method returned [`true`](../../Swift/true.md).

## Parameters

- `tableView`: The table view from which the drag operation originated.
- `session`: The drag session object containing information about the drag operation.

## See Also

### Tracking the drag session
- [func tableView(UITableView, dragSessionWillBegin: any UIDragSession)](./tableview%28_,dragsessionwillbegin%29.md)
  Signals the start of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionDidEnd: any UIDragSession)](./tableview%28_,dragsessiondidend%29.md)
  Signals the end of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](./tableview%28_,dragsessionisrestrictedtodraggingapplication%29.md)
  Returns a Boolean value indicating whether the dragged content must be dropped in the same app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionallowsmoveoperation:))*