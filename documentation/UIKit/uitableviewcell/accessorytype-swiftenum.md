# UITableViewCell.AccessoryType

**Framework**: UIKit  
**Kind**: enum

The type of standard accessory control used by a cell.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum AccessoryType
```

## Mentions

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)

#### Overview

Use these constants to set the value of the [`accessoryType`](uitableviewcell/accessorytype-swift.property.md) property.

Several accessory views support additional interactions. For example, a detail button conveys that there is additional information for the user to see. For information about how to respond to interactions with a specific accessory view, see the discussion for that type.

## Topics

### Accessory views
- [UITableViewCell.AccessoryType.none](uitableviewcell/accessorytype-swift.enum/none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.disclosureIndicator](uitableviewcell/accessorytype-swift.enum/disclosureindicator.md)
  A chevron-shaped control for presenting new content.
- [UITableViewCell.AccessoryType.detailDisclosureButton](uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton.md)
  An information button and a disclosure (chevron) control.
- [UITableViewCell.AccessoryType.checkmark](uitableviewcell/accessorytype-swift.enum/checkmark.md)
  A checkmark image.
- [UITableViewCell.AccessoryType.detailButton](uitableviewcell/accessorytype-swift.enum/detailbutton.md)
  An information button.
### Initializers
- [init?(rawValue: Int)](uitableviewcell/accessorytype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var accessoryType: UITableViewCell.AccessoryType](uitableviewcell/accessorytype-swift.property.md)
  The type of standard accessory view for the cell to use in the table view’s normal state.
- [var accessoryView: UIView?](uitableviewcell/accessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [var editingAccessoryType: UITableViewCell.AccessoryType](uitableviewcell/editingaccessorytype.md)
  The type of standard accessory view for the cell to use in the table view’s editing state.
- [var editingAccessoryView: UIView?](uitableviewcell/editingaccessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s editing state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum)*