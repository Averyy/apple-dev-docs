# UITableViewDropCoordinator

**Framework**: UIKit  
**Kind**: protocol

An interface for coordinating your custom drop-related actions with the table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITableViewDropCoordinator : NSObjectProtocol
```

## Mentions

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

#### Overview

Don’t create instances of this class yourself. When a drop occurs in the table view, UIKit creates an instance of this class and passes it to your [`tableView(_:performDropWith:)`](uitableviewdropdelegate/tableview(_:performdropwith:).md) method. Use the object to let the table view know how you want to animate the dropped items into position.

## Topics

### Getting the dragged items
- [var items: [any UITableViewDropItem]](uitableviewdropcoordinator/items.md)
  The items being dragged.
### Getting the drop location
- [var destinationIndexPath: IndexPath?](uitableviewdropcoordinator/destinationindexpath.md)
  The index path at which to insert the item into the table view.
### Animating rows to their destination
- [func drop(UIDragItem, toRowAt: IndexPath) -> any UIDragAnimating](uitableviewdropcoordinator/drop(_:torowat:).md)
  Animates the item to the specified index path in the table view.
- [func drop(UIDragItem, intoRowAt: IndexPath, rect: CGRect) -> any UIDragAnimating](uitableviewdropcoordinator/drop(_:intorowat:rect:).md)
- [func drop(UIDragItem, to: UIDragPreviewTarget) -> any UIDragAnimating](uitableviewdropcoordinator/drop(_:to:)-57wx.md)
  Animates the item to an arbitrary location in your view hierarchy.
- [func drop(UIDragItem, to: UITableViewDropPlaceholder) -> any UITableViewDropPlaceholderContext](uitableviewdropcoordinator/drop(_:to:)-3znax.md)
  Animates the item to the specified location and inserts a placeholder cell at that location.
### Getting the session information
- [var session: any UIDropSession](uitableviewdropcoordinator/session.md)
  The drop session containing information about the transaction.
- [var proposal: UITableViewDropProposal](uitableviewdropcoordinator/proposal.md)
  The proposal for how to incorporate the dropped items.

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
- [protocol UITableViewDropItem](uitableviewdropitem.md)
  The data associated with an item being dropped into the table view.
- [class UITableViewDropProposal](uitableviewdropproposal.md)
  Your proposed solution for handling a drop in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropcoordinator)*