# tableView(_:dragSessionAllowsMoveOperation:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value indicating whether your app supports a move operation for the dragged content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, dragSessionAllowsMoveOperation session: any UIDragSession) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if your app allows content to be moved instead of copied, or [`false`](https://developer.apple.com/documentation/swift/false) if moves are not supported.

#### Discussion

Implement this method if you want to prevent the dragged content from being moved. If your delegate returns [`false`](https://developer.apple.com/documentation/swift/false) and the drop operation type is [`UIDropOperation.move`](uidropoperation/move.md), the system cancels the drop.

If you don’t implement this method, the table view behaves as if the method returned [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `tableView`: The table view from which the drag operation originated.
- `session`: The drag session object containing information about the drag operation.

## See Also

- [func tableView(UITableView, dragSessionWillBegin: any UIDragSession)](uitableviewdragdelegate/tableview(_:dragsessionwillbegin:).md)
  Signals the start of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionDidEnd: any UIDragSession)](uitableviewdragdelegate/tableview(_:dragsessiondidend:).md)
  Signals the end of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](uitableviewdragdelegate/tableview(_:dragsessionisrestrictedtodraggingapplication:).md)
  Returns a Boolean value indicating whether the dragged content must be dropped in the same app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionallowsmoveoperation:))*