# tableView(_:dropSessionDidEnd:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate when the drag operation ends.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, dropSessionDidEnd session: any UIDropSession)
```

#### Discussion

The table view calls this method at the conclusion of a drag that was over the table view at one point. Use it to clean up any state information that you used to handle the drag. This method is called regardless of whether the data was actually dropped onto the table view.

## Parameters

- `tableView`: The table view that is no longer the target of the drop.
- `session`: The drop session object containing information about the data being dragged.

## See Also

- [func tableView(UITableView, dropSessionDidUpdate: any UIDropSession, withDestinationIndexPath: IndexPath?) -> UITableViewDropProposal](uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:).md)
  Proposes how to handle a drop at the specified location in the table view.
- [func tableView(UITableView, dropSessionDidEnter: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidenter:).md)
  Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [func tableView(UITableView, dropSessionDidExit: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidexit:).md)
  Notifies the delegate when dragged content exits the table view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropdelegate/tableview(_:dropsessiondidend:))*