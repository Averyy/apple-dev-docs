# dragDelegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate object that manages the dragging of items from the table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var dragDelegate: (any UITableViewDragDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UITableViewDragDelegate> dragDelegate;
```

## Mentions

- [Supporting drag and drop in table views](../supporting-drag-and-drop-in-table-views.md)

## See Also

### Managing drag interactions
- [protocol UITableViewDragDelegate](../uitableviewdragdelegate.md)
  The interface for initiating drags from a table view.
- [var hasActiveDrag: Bool](./hasactivedrag.md)
  A Boolean value that indicates whether the table view is currently tracking a drag session.
- [var dragInteractionEnabled: Bool](./draginteractionenabled.md)
  A Boolean value that indicates whether the table view supports dragging content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/dragdelegate)*