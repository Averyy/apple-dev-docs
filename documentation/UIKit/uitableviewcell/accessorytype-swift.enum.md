# UITableViewCell.AccessoryType

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The type of standard accessory control used by a cell.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum AccessoryType
```

```c
enum UITableViewCellAccessoryType : NSInteger;
```

## Mentions

- [Configuring the cells for your table](../configuring-the-cells-for-your-table.md)

## Overview

Use these constants to set the value of the [`accessoryType`](./accessorytype-swift.property.md) property.

Several accessory views support additional interactions. For example, a detail button conveys that there is additional information for the user to see. For information about how to respond to interactions with a specific accessory view, see the discussion for that type.

## Topics

### Accessory views
- [UITableViewCell.AccessoryType.none](./accessorytype-swift.enum/none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.disclosureIndicator](./accessorytype-swift.enum/disclosureindicator.md)
  A chevron-shaped control for presenting new content.
- [UITableViewCell.AccessoryType.detailDisclosureButton](./accessorytype-swift.enum/detaildisclosurebutton.md)
  An information button and a disclosure (chevron) control.
- [UITableViewCell.AccessoryType.checkmark](./accessorytype-swift.enum/checkmark.md)
  A checkmark image.
- [UITableViewCell.AccessoryType.detailButton](./accessorytype-swift.enum/detailbutton.md)
  An information button.
### Initializers
- [init?(rawValue: Int)](./accessorytype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing accessory views
- [var accessoryType: UITableViewCell.AccessoryType](./accessorytype-swift.property.md)
  The type of standard accessory view for the cell to use in the table view’s normal state.
- [var accessoryView: UIView?](./accessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [var editingAccessoryType: UITableViewCell.AccessoryType](./editingaccessorytype.md)
  The type of standard accessory view for the cell to use in the table view’s editing state.
- [var editingAccessoryView: UIView?](./editingaccessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s editing state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum)*