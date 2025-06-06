# UITableViewFocusUpdateContext

**Framework**: UIKit  
**Kind**: class

A context object that provides information relevant to a specific focus update from one view to another.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITableViewFocusUpdateContext
```

#### Overview

A focus update context provides extra information that’s only relevant to focus updates involving table views. Instances of this class are ephemeral and are usually discarded after the update is finished.

## Topics

### Locating focusable items in a table view
- [var previouslyFocusedIndexPath: IndexPath?](uitableviewfocusupdatecontext/previouslyfocusedindexpath.md)
  Returns the index path of the cell containing the context’s previously focused view.
- [var nextFocusedIndexPath: IndexPath?](uitableviewfocusupdatecontext/nextfocusedindexpath.md)
  Returns the index path of the cell containing the context’s next focused view.

## Relationships

### Inherits From
- [UIFocusUpdateContext](uifocusupdatecontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md)
  Provide height estimates for your table view’s headers, footers, and rows to ensure that scrolling accurately reflects the size of your content.
- [class UITableViewController](uitableviewcontroller.md)
  A view controller that specializes in managing a table view.
- [protocol UITableViewDelegate](uitableviewdelegate.md)
  Methods for managing selections, configuring section headers and footers, deleting and reordering cells, and performing other actions in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext)*