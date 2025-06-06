# UITableViewDropDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for handling drops in a table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITableViewDropDelegate : NSObjectProtocol
```

## Mentions

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

#### Overview

Implement this protocol in the object that you use to incorporate dropped data into your table view. The only required method of this protocol is the [`tableView(_:performDropWith:)`](uitableviewdropdelegate/tableview(_:performdropwith:).md) method, but you can implement other methods as needed to customize the drop behavior of your table view.

Assign your custom delegate object to the [`dropDelegate`](uitableview/dropdelegate.md) property of your table view.

## Topics

### Declaring support for handling drops
- [func tableView(UITableView, canHandle: any UIDropSession) -> Bool](uitableviewdropdelegate/tableview(_:canhandle:).md)
  Asks your delegate whether it can accept the specified type of data.
### Providing a custom drop preview
- [func tableView(UITableView, dropPreviewParametersForRowAt: IndexPath) -> UIDragPreviewParameters?](uitableviewdropdelegate/tableview(_:droppreviewparametersforrowat:).md)
  Returns custom information about how to display the row at the specified location during the drop.
### Incorporating the dropped data
- [func tableView(UITableView, performDropWith: any UITableViewDropCoordinator)](uitableviewdropdelegate/tableview(_:performdropwith:).md)
  Incorporates the dropped data into your data structures and updates the table.
### Tracking the drag movements
- [func tableView(UITableView, dropSessionDidUpdate: any UIDropSession, withDestinationIndexPath: IndexPath?) -> UITableViewDropProposal](uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:).md)
  Proposes how to handle a drop at the specified location in the table view.
- [func tableView(UITableView, dropSessionDidEnter: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidenter:).md)
  Notifies the delegate when dragged content enters the table view’s bounds rectangle.
- [func tableView(UITableView, dropSessionDidExit: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidexit:).md)
  Notifies the delegate when dragged content exits the table view’s bounds rectangle.
- [func tableView(UITableView, dropSessionDidEnd: any UIDropSession)](uitableviewdropdelegate/tableview(_:dropsessiondidend:).md)
  Notifies the delegate when the drag operation ends.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)
  Initiate drags and handle drops from a table view.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md)
  Demonstrates how to enable and implement drag and drop for a table view.
- [protocol UITableViewDragDelegate](uitableviewdragdelegate.md)
  The interface for initiating drags from a table view.
- [protocol UITableViewDropCoordinator](uitableviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the table view.
- [protocol UITableViewDropItem](uitableviewdropitem.md)
  The data associated with an item being dropped into the table view.
- [class UITableViewDropProposal](uitableviewdropproposal.md)
  Your proposed solution for handling a drop in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropdelegate)*