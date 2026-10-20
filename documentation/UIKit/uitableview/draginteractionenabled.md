# dragInteractionEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the table view supports dragging content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var dragInteractionEnabled: Bool { get set }
```

```objc
@property (nonatomic) BOOL dragInteractionEnabled;
```

#### Discussion

To support dragging content from the table view to a view in your app or another app, set this property value to [`true`](../../Swift/true.md). To disable this behavior, set the value to [`false`](../../Swift/false.md). The default value is [`true`](../../Swift/true.md).

In iOS 14 and earlier, the default value is [`true`](../../Swift/true.md) for iPad and [`false`](../../Swift/false.md) for iPhone. Setting the value to [`true`](../../Swift/true.md) on iPhone enables dragging within your app only. Dragging content to other apps isn’t possible on iPhone prior to iOS 15.

## See Also

### Managing drag interactions
- [var dragDelegate: (any UITableViewDragDelegate)?](./dragdelegate.md)
  The delegate object that manages the dragging of items from the table view.
- [protocol UITableViewDragDelegate](../uitableviewdragdelegate.md)
  The interface for initiating drags from a table view.
- [var hasActiveDrag: Bool](./hasactivedrag.md)
  A Boolean value that indicates whether the table view is currently tracking a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/draginteractionenabled)*