# UITableViewCell.DragState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UITableViewCellDragState : NSInteger;
```

## Topics

### Constants
- [UITableViewCell.DragState.none](./dragstate/none.md)
  The cell isn’t involved in a drag operation.
- [UITableViewCell.DragState.lifting](./dragstate/lifting.md)
  The cell is being animated off of the table’s surface.
- [UITableViewCell.DragState.dragging](./dragstate/dragging.md)
  The cell is currently being dragged.
### Initializers
- [init?(rawValue: Int)](./dragstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Dragging the row
- [var userInteractionEnabledWhileDragging: Bool](./userinteractionenabledwhiledragging.md)
  A Boolean value indicating whether users can interact with a cell while it is being dragged.
- [func dragStateDidChange(UITableViewCell.DragState)](./dragstatedidchange%28_%29.md)
  Notifies the cell that its drag status changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/dragstate)*