# UITableViewDropPlaceholderContext

**Framework**: UIKit  
**Kind**: protocol

An object for tracking a placeholder cell that you added to your table during a drop operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITableViewDropPlaceholderContext : UIDragAnimating
```

#### Overview

Don’t create instances of this class yourself. Instead, call [`drop(_:to:)`](uitableviewdropcoordinator/drop(_:to:)-3znax.md) from your drop coordinator object. That method inserts a placeholder cell into the table and returns a [`UITableViewDropPlaceholderContext`](uitableviewdropplaceholdercontext.md) object for managing that placeholder.

When you’re ready to swap a placeholder cell for a cell with the actual data, call the [`commitInsertion(dataSourceUpdates:)`](uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates:).md) method of the context object. To remove the placeholder cell without providing a replacement, call [`deletePlaceholder()`](uitableviewdropplaceholdercontext/deleteplaceholder().md) instead.

## Topics

### Updating the placeholder cell
- [func commitInsertion(dataSourceUpdates: (IndexPath) -> Void) -> Bool](uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates:).md)
  Exchanges the placeholder cell for a cell with the final content.
### Removing the placeholder cell
- [func deletePlaceholder() -> Bool](uitableviewdropplaceholdercontext/deleteplaceholder.md)
  Removes an unneeded placeholder cell from the table view.
### Getting the drag item
- [var dragItem: UIDragItem](uitableviewdropplaceholdercontext/dragitem.md)
  The drag item represented by the placeholder cell.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIDragAnimating](uidraganimating.md)

## See Also

- [class UITableViewDropPlaceholder](uitableviewdropplaceholder.md)
  A placeholder cell that supports customizing the drop preview parameters.
- [class UITableViewPlaceholder](uitableviewplaceholder.md)
  An object that contains information about a placeholder cell being inserted into a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropplaceholdercontext)*