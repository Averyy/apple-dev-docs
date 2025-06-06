# tableView(_:dragSessionWillBegin:)

**Framework**: UIKit  
**Kind**: method

Signals the start of a drag operation involving content from the specified table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, dragSessionWillBegin session: any UIDragSession)
```

#### Discussion

This method is called after it has been determined that a drag will begin, after any lift animations have occurred, and before the position of the drag changes significantly. Use this method to perform any tasks related to the management of the drag session in your app.

Each call to this method is always balanced by a call to the [`tableView(_:dragSessionDidEnd:)`](uitableviewdragdelegate/tableview(_:dragsessiondidend:).md) method.

## Parameters

- `tableView`: The table view from which the drag operation originated.
- `session`: The drag session object providing context for the drag operation.

## See Also

- [func tableView(UITableView, dragSessionDidEnd: any UIDragSession)](uitableviewdragdelegate/tableview(_:dragsessiondidend:).md)
  Signals the end of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](uitableviewdragdelegate/tableview(_:dragsessionisrestrictedtodraggingapplication:).md)
  Returns a Boolean value indicating whether the dragged content must be dropped in the same app.
- [func tableView(UITableView, dragSessionAllowsMoveOperation: any UIDragSession) -> Bool](uitableviewdragdelegate/tableview(_:dragsessionallowsmoveoperation:).md)
  Returns a Boolean value indicating whether your app supports a move operation for the dragged content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdragdelegate/tableview(_:dragsessionwillbegin:))*