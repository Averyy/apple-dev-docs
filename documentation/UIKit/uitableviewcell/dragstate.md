# UITableViewCell.DragState

**Framework**: UIKit  
**Kind**: enum

Constants indicating the current state of a row involved in a drag operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum DragState
```

## Topics

### Constants
- [UITableViewCell.DragState.none](uitableviewcell/dragstate/none.md)
  The cell isn’t involved in a drag operation.
- [UITableViewCell.DragState.lifting](uitableviewcell/dragstate/lifting.md)
  The cell is being animated off of the table’s surface.
- [UITableViewCell.DragState.dragging](uitableviewcell/dragstate/dragging.md)
  The cell is currently being dragged.
### Initializers
- [init?(rawValue: Int)](uitableviewcell/dragstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var userInteractionEnabledWhileDragging: Bool](uitableviewcell/userinteractionenabledwhiledragging.md)
  A Boolean value indicating whether users can interact with a cell while it is being dragged.
- [func dragStateDidChange(UITableViewCell.DragState)](uitableviewcell/dragstatedidchange(_:).md)
  Notifies the cell that its drag status changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/dragstate)*