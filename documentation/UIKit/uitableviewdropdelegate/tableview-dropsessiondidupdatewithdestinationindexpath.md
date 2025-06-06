# tableView(_:dropSessionDidUpdate:withDestinationIndexPath:)

**Framework**: UIKit  
**Kind**: method

Proposes how to handle a drop at the specified location in the table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, dropSessionDidUpdate session: any UIDropSession, withDestinationIndexPath destinationIndexPath: IndexPath?) -> UITableViewDropProposal
```

## Mentions

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

#### Return Value

The [`UITableViewDropProposal`](uitableviewdropproposal.md) object indicating how to incorporate the dropped data.

#### Discussion

While the user is dragging content, the table view calls this method repeatedly to determine how you would handle the drop if it occurred at the specified location. The table view provides visual feedback to the user based on your proposal.

In your implementation of this method, create a [`UITableViewDropProposal`](uitableviewdropproposal.md) object and use it to convey your intentions. Because this method is called repeatedly while the user drags over the table view, your implementation should return as quickly as possible.

## Parameters

- `tableView`: The table view currently being targeted to receive the drop.
- `session`: The drop session object containing information about the data being dragged.
- `destinationIndexPath`: The index path of the row currently being targeted by the drop. Use this value to determine an appropriate course of action for the drop.

## See Also

- [func tableView(UITableView, dropSessionDidEnter: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidenter:).md)
  Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [func tableView(UITableView, dropSessionDidExit: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidexit:).md)
  Notifies the delegate when dragged content exits the table view’s bounds rectangle.
- [func tableView(UITableView, dropSessionDidEnd: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidend:).md)
  Notifies the delegate when the drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:))*