# dragStateDidChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the cell that its drag status changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func dragStateDidChange(_ dragState: UITableViewCell.DragState)
```

```objc
- (void) dragStateDidChange:(UITableViewCellDragState) dragState;
```

## Parameters

- `dragState`: The new drag state for the cell.

## See Also

### Dragging the row
- [var userInteractionEnabledWhileDragging: Bool](./userinteractionenabledwhiledragging.md)
  A Boolean value indicating whether users can interact with a cell while it is being dragged.
- [UITableViewCell.DragState](./dragstate.md)
  Constants indicating the current state of a row involved in a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/dragstatedidchange(_:))*