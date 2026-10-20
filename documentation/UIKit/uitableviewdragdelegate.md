# UITableViewDragDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface for initiating drags from a table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITableViewDragDelegate : NSObjectProtocol
```

```objc
@protocol UITableViewDragDelegate <NSObject>
```

## Mentions

- [Supporting drag and drop in table views](./supporting-drag-and-drop-in-table-views.md)

#### Overview

Implement this protocol in the object that you use to initiate drags from your table view. The only required method of this protocol is the [`tableView(_:itemsForBeginning:at:)`](./uitableviewdragdelegate/tableview%28_,itemsforbeginning,at%29.md) method, but you can implement other methods as needed to customize the drag behavior of your table view.

Assign your custom delegate object to the [`dragDelegate`](./uitableview/dragdelegate.md) property of your table view.

## Topics

### Providing the items to drag
- [func tableView(UITableView, itemsForBeginning: any UIDragSession, at: IndexPath) -> [UIDragItem]](./uitableviewdragdelegate/tableview%28_,itemsforbeginning,at%29.md)
  Provides the initial set of items (if any) to drag.
- [func tableView(UITableView, itemsForAddingTo: any UIDragSession, at: IndexPath, point: CGPoint) -> [UIDragItem]](./uitableviewdragdelegate/tableview%28_,itemsforaddingto,at,point%29.md)
  Adds the specified items to an existing drag session.
### Tracking the drag session
- [func tableView(UITableView, dragSessionWillBegin: any UIDragSession)](./uitableviewdragdelegate/tableview%28_,dragsessionwillbegin%29.md)
  Signals the start of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionDidEnd: any UIDragSession)](./uitableviewdragdelegate/tableview%28_,dragsessiondidend%29.md)
  Signals the end of a drag operation involving content from the specified table view.
- [func tableView(UITableView, dragSessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](./uitableviewdragdelegate/tableview%28_,dragsessionisrestrictedtodraggingapplication%29.md)
  Returns a Boolean value indicating whether the dragged content must be dropped in the same app.
- [func tableView(UITableView, dragSessionAllowsMoveOperation: any UIDragSession) -> Bool](./uitableviewdragdelegate/tableview%28_,dragsessionallowsmoveoperation%29.md)
  Returns a Boolean value indicating whether your app supports a move operation for the dragged content.
### Providing a custom preview
- [func tableView(UITableView, dragPreviewParametersForRowAt: IndexPath) -> UIDragPreviewParameters?](./uitableviewdragdelegate/tableview%28_,dragpreviewparametersforrowat%29.md)
  Returns custom information about how to display the row at the specified location during the drag.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Drag and drop
- [Supporting drag and drop in table views](./supporting-drag-and-drop-in-table-views.md)
  Initiate drags and handle drops from a table view.
- [Adopting drag and drop in a table view](./adopting-drag-and-drop-in-a-table-view.md)
  Demonstrates how to enable and implement drag and drop for a table view.
- [protocol UITableViewDropDelegate](./uitableviewdropdelegate.md)
  The interface for handling drops in a table view.
- [protocol UITableViewDropCoordinator](./uitableviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the table view.
- [protocol UITableViewDropItem](./uitableviewdropitem.md)
  The data associated with an item being dropped into the table view.
- [class UITableViewDropProposal](./uitableviewdropproposal.md)
  Your proposed solution for handling a drop in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdragdelegate)*