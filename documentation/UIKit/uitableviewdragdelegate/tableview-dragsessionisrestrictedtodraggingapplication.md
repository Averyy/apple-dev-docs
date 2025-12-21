# tableView(_:dragSessionIsRestrictedToDraggingApplication:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value indicating whether the dragged content must be dropped in the same app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, dragSessionIsRestrictedToDraggingApplication session: any UIDragSession) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the dragged content must be dropped in the same app that originated the drag, or [`false`](https://developer.apple.com/documentation/Swift/false) if the content may be dragged to other apps.

#### Discussion

Implement this method when you want to allow the user to drag content within your app, but prevent them from dragging that same content to other apps. If you don’t implement this method, the table view behaves as if the method returned [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `tableView`: The table view from which the drag operation originated.
- `session`: The drag session object containing information about the drag operation.

## See Also

- [func tableView(UITableView, dragSessionWillBegin: any UIDragSession)](uitableviewdragdelegate/tableview(_:dragsessionwillbegin:).md)
  Signals the start of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionDidEnd: any UIDragSession)](uitableviewdragdelegate/tableview(_:dragsessiondidend:).md)
  Signals the end of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionAllowsMoveOperation: any UIDragSession) -> Bool](uitableviewdragdelegate/tableview(_:dragsessionallowsmoveoperation:).md)
  Returns a Boolean value indicating whether your app supports a move operation for the dragged content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionisrestrictedtodraggingapplication:))*