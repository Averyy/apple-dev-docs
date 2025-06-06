# UITableViewDropItem

**Framework**: UIKit  
**Kind**: protocol

The data associated with an item being dropped into the table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITableViewDropItem : NSObjectProtocol
```

#### Overview

When handling a drop, you get instances of this class from the [`items`](uitableviewdropcoordinator/items.md) property of the [`UITableViewDropCoordinator`](uitableviewdropcoordinator.md) object. Use them to retrieve the data for the items being dragged and to plan any animations related to dropping the items. You don’t create instances of this class yourself.

## Topics

### Getting the drag item
- [var dragItem: UIDragItem](uitableviewdropitem/dragitem.md)
  The item that was dragged.
### Getting the item information
- [var previewSize: CGSize](uitableviewdropitem/previewsize.md)
  The size of the drag item’s preview.
- [var sourceIndexPath: IndexPath?](uitableviewdropitem/sourceindexpath.md)
  The index path of the item in the table view, if any.

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
- [protocol UITableViewDropDelegate](uitableviewdropdelegate.md)
  The interface for handling drops in a table view.
- [protocol UITableViewDropCoordinator](uitableviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the table view.
- [class UITableViewDropProposal](uitableviewdropproposal.md)
  Your proposed solution for handling a drop in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropitem)*