# tableView(_:dropSessionDidExit:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate when dragged content exits the table view’s bounds rectangle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, dropSessionDidExit session: any UIDropSession)
```

#### Discussion

The table view calls this method when dragged content exits its bounds rectangle. This method isn’t called again until the dragged content enters the table view’s bounds (triggering a call to the [`tableView(_:dropSessionDidEnter:)`](uitableviewdropdelegate/tableview(_:dropsessiondidenter:).md) method) and exits again.

Use this method to clean up any state information that you configured in your [`tableView(_:dropSessionDidEnter:)`](uitableviewdropdelegate/tableview(_:dropsessiondidenter:).md) method.

## Parameters

- `tableView`: The collection view that was tracking the dragged content.
- `session`: The drop session object containing information about the data being dragged.

## See Also

- [func tableView(UITableView, dropSessionDidUpdate: any UIDropSession, withDestinationIndexPath: IndexPath?) -> UITableViewDropProposal](uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:).md)
  Proposes how to handle a drop at the specified location in the table view.
- [func tableView(UITableView, dropSessionDidEnter: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidenter:).md)
  Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [func tableView(UITableView, dropSessionDidEnd: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidend:).md)
  Notifies the delegate when the drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidexit:))*