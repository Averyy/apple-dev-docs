# tableView(_:dropSessionDidEnter:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate when dragged content enters the table view’s bounds rectangle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, dropSessionDidEnter session: any UIDropSession)
```

#### Discussion

The table view calls this method when dragged content first enters its bounds rectangle. This method isn’t called again until the dragged content exits the table view’s bounds (triggering a call to the [`tableView(_:dropSessionDidExit:)`](uitableviewdropdelegate/tableview(_:dropsessiondidexit:).md) method) and enters again.

Use this method to perform any one-time setup associated with tracking dragged content over the table view.

## Parameters

- `tableView`: The table view that’s now the potential target of the drop.
- `session`: The drop session object containing information about the data being dragged.

## See Also

- [func tableView(UITableView, dropSessionDidUpdate: any UIDropSession, withDestinationIndexPath: IndexPath?) -> UITableViewDropProposal](uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:).md)
  Proposes how to handle a drop at the specified location in the table view.
- [func tableView(UITableView, dropSessionDidExit: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidexit:).md)
  Notifies the delegate when dragged content exits the table view’s bounds rectangle.
- [func tableView(UITableView, dropSessionDidEnd: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidend:).md)
  Notifies the delegate when the drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidenter:))*