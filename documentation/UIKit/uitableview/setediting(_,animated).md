# setEditing(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Toggles the table view into and out of editing mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setEditing(_ editing: Bool, animated: Bool)
```

```objc
- (void) setEditing:(BOOL) editing animated:(BOOL) animated;
```

## Discussion

When you call this method with the value of `editing` set to [`true`](../../Swift/true.md), the table view goes into editing mode by calling [`setEditing(_:animated:)`](../uitableviewcell/setediting%28_,animated%29.md) on each visible `UITableViewCell` object. Calling this method with `editing` set to [`false`](../../Swift/false.md) turns off editing mode. In editing mode, the cells of the table might show an insertion or deletion control on the left side of each cell and a reordering control on the right side, depending on how the cell is configured. (See [`UITableViewCell`](../uitableviewcell.md) for details.) The data source of the table view can selectively exclude cells from editing mode by implementing [`tableView(_:canEditRowAt:)`](../uitableviewdatasource/tableview%28_,caneditrowat%29.md).

## Parameters

- `editing`: [`true`](../../Swift/true.md) to enter editing mode; [`false`](../../Swift/false.md) to leave it. The default value is [`false`](../../Swift/false.md).
- `animated`: [`true`](../../Swift/true.md) to animate the transition to editing mode; [`false`](../../Swift/false.md) to make the transition immediate.

## See Also

### Putting the table into edit mode
- [var isEditing: Bool](./isediting.md)
  A Boolean value that determines whether the table view is in editing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/setediting(_:animated:))*