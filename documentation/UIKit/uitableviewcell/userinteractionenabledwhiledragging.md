# userInteractionEnabledWhileDragging

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether users can interact with a cell while it is being dragged.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var userInteractionEnabledWhileDragging: Bool { get set }
```

```objc
@property (nonatomic) BOOL userInteractionEnabledWhileDragging;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Dragging the row
- [func dragStateDidChange(UITableViewCell.DragState)](./dragstatedidchange%28_%29.md)
  Notifies the cell that its drag status changed.
- [UITableViewCell.DragState](./dragstate.md)
  Constants indicating the current state of a row involved in a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/userinteractionenabledwhiledragging)*