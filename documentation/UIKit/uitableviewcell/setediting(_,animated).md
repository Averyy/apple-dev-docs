# setEditing(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Toggles the cell into and out of editing mode.

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

#### Discussion

When you call this method with the value of `editing` set to [`true`](../../Swift/true.md), and the `UITableViewCell` object is configured to have controls, the cell shows an insertion (green plus) or deletion control (red minus) on the left side of each cell and a reordering control on the right side. This method is called on each visible cell when the [`setEditing(_:animated:)`](../uitableview/setediting%28_,animated%29.md) method of `UITableView` is invoked. Calling this method with `editing` set to [`false`](../../Swift/false.md) removes the controls from the cell.

## Parameters

- `editing`: [`true`](../../Swift/true.md) to enter editing mode, [`false`](../../Swift/false.md) to leave it. The default value is [`false`](../../Swift/false.md).
- `animated`: [`true`](../../Swift/true.md) to animate the appearance or disappearance of the insertion/deletion control and the reordering control, [`false`](../../Swift/false.md) to make the transition immediate.

## See Also

### Editing the cell
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the cell is in an editable state.
- [var editingStyle: UITableViewCell.EditingStyle](./editingstyle-swift.property.md)
  The editing style of the cell.
- [UITableViewCell.EditingStyle](./editingstyle-swift.enum.md)
  The editing control used by a cell.
- [var showingDeleteConfirmation: Bool](./showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [var showsReorderControl: Bool](./showsreordercontrol.md)
  A Boolean value that determines whether the cell shows the reordering control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/setediting(_:animated:))*