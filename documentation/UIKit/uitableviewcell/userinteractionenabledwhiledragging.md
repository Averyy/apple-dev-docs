# userInteractionEnabledWhileDragging

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether users can interact with a cell while it is being dragged.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var userInteractionEnabledWhileDragging: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func dragStateDidChange(UITableViewCell.DragState)](uitableviewcell/dragstatedidchange(_:).md)
  Notifies the cell that its drag status changed.
- [UITableViewCell.DragState](uitableviewcell/dragstate.md)
  Constants indicating the current state of a row involved in a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/userinteractionenabledwhiledragging)*