# editingAccessoryType

**Framework**: UIKit  
**Kind**: property

The type of standard accessory view for the cell to use in the table view’s editing state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var editingAccessoryType: UITableViewCell.AccessoryType { get set }
```

#### Discussion

The accessory view appears in the right side of the cell when the table view is in editing mode. The standard accessory views include the disclosure chevron; for a description of valid constants, see [`UITableViewCell.AccessoryType`](uitableviewcell/accessorytype-swift.enum.md). The default is [`UITableViewCell.AccessoryType.none`](uitableviewcell/accessorytype-swift.enum/none.md). If a custom accessory view for editing mode is set through the [`editingAccessoryView`](uitableviewcell/editingaccessoryview.md) property, the value of this property is ignored. If the cell is enabled and the accessory type is [`UITableViewCell.AccessoryType.detailDisclosureButton`](uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton.md), the accessory view tracks touches and, when tapped, sends the delegate object a [`tableView(_:accessoryButtonTappedForRowWith:)`](uitableviewdelegate/tableview(_:accessorybuttontappedforrowwith:).md) message.

The accessory type cross-fades between normal and editing states if it set for both states; use the [`accessoryType`](uitableviewcell/accessorytype-swift.property.md) property to set the accessory view for the cell during the table view’s normal state. If this property is not set for both states, the cell is animated to slide or out, as necessary.

## See Also

- [func willTransition(to: UITableViewCell.StateMask)](uitableviewcell/willtransition(to:).md)
  Notifies the cell that it’s about to transition to a new cell state.
- [func didTransition(to: UITableViewCell.StateMask)](uitableviewcell/didtransition(to:).md)
  Notifies the cell that it transitioned to a new cell state.
- [var accessoryType: UITableViewCell.AccessoryType](uitableviewcell/accessorytype-swift.property.md)
  The type of standard accessory view for the cell to use in the table view’s normal state.
- [var accessoryView: UIView?](uitableviewcell/accessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [var editingAccessoryView: UIView?](uitableviewcell/editingaccessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
- [UITableViewCell.AccessoryType](uitableviewcell/accessorytype-swift.enum.md)
  The type of standard accessory control used by a cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/editingaccessorytype)*