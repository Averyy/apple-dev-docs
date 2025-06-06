# accessoryView

**Framework**: UIKit  
**Kind**: property

The view to use on the right side of the cell, typically as a control, in the table view’s normal state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var accessoryView: UIView? { get set }
```

#### Discussion

If the value of this property is not `nil`, the `UITableViewCell` class uses the given view for the accessory view in the table view’s normal (default) state; it ignores the value of the [`accessoryType`](uitableviewcell/accessorytype-swift.property.md) property. The provided accessory view can be a framework-provided control or label or a custom view. The accessory view appears in the right side of the cell.

The accessory view cross-fades between normal and editing states if it set for both states; use the [`editingAccessoryView`](uitableviewcell/editingaccessoryview.md) property to set the accessory view for the cell during editing mode. If this property is not set for both states, the cell is animated to slide in or out, as necessary.

## See Also

- [func willTransition(to: UITableViewCell.StateMask)](uitableviewcell/willtransition(to:).md)
  Notifies the cell that it’s about to transition to a new cell state.
- [func didTransition(to: UITableViewCell.StateMask)](uitableviewcell/didtransition(to:).md)
  Notifies the cell that it transitioned to a new cell state.
- [var accessoryType: UITableViewCell.AccessoryType](uitableviewcell/accessorytype-swift.property.md)
  The type of standard accessory view for the cell to use in the table view’s normal state.
- [var editingAccessoryType: UITableViewCell.AccessoryType](uitableviewcell/editingaccessorytype.md)
  The type of standard accessory view for the cell to use in the table view’s editing state.
- [var editingAccessoryView: UIView?](uitableviewcell/editingaccessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
- [UITableViewCell.AccessoryType](uitableviewcell/accessorytype-swift.enum.md)
  The type of standard accessory control used by a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessoryview)*