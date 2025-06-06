# UITableViewPlaceholder

**Framework**: UIKit  
**Kind**: class

An object that contains information about a placeholder cell being inserted into a table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITableViewPlaceholder
```

#### Overview

During a drop operation, create a [`UITableViewDropPlaceholder`](uitableviewdropplaceholder.md) object (instead of this one) to insert placeholders into your table.

## Topics

### Creating a placeholder cell
- [init(insertionIndexPath: IndexPath, reuseIdentifier: String, rowHeight: CGFloat)](uitableviewplaceholder/init(insertionindexpath:reuseidentifier:rowheight:).md)
  Creates a placeholder object with the specified index path and cell-related information.
### Updating the cell’s content
- [var cellUpdateHandler: ((UITableViewCell) -> Void)?](uitableviewplaceholder/cellupdatehandler.md)
  The block that updates the contents of the placeholder cell.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UITableViewDropPlaceholder](uitableviewdropplaceholder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md)
  An object for tracking a placeholder cell that you added to your table during a drop operation.
- [class UITableViewDropPlaceholder](uitableviewdropplaceholder.md)
  A placeholder cell that supports customizing the drop preview parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewplaceholder)*