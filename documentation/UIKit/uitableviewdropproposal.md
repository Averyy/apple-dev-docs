# UITableViewDropProposal

**Framework**: UIKit  
**Kind**: class

Your proposed solution for handling a drop in a table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITableViewDropProposal
```

## Mentions

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

#### Overview

Create instances of this class in the [`tableView(_:dropSessionDidUpdate:withDestinationIndexPath:)`](uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:).md) method of your drop delegate object. You create drop proposals to let the table view know how you intend to handle a drop at the currently specified location. The table view uses that information to provide appropriate visual feedback to the user.

## Topics

### Creating a drop proposal
- [init(operation: UIDropOperation, intent: UITableViewDropProposal.Intent)](uitableviewdropproposal/init(operation:intent:).md)
  Creates a drop proposal object that specifies how to incorporate the dropped content.
### Getting the proposed drop location
- [var intent: UITableViewDropProposal.Intent](uitableviewdropproposal/intent-swift.property.md)
  The option to use when incorporating dropped items into your content.
- [UITableViewDropProposal.Intent](uitableviewdropproposal/intent-swift.enum.md)
  Constants indicating how you intend to handle a drop.
- [enum UIDropOperation](uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.

## Relationships

### Inherits From
- [UIDropProposal](uidropproposal.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

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
- [protocol UITableViewDropItem](uitableviewdropitem.md)
  The data associated with an item being dropped into the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropproposal)*