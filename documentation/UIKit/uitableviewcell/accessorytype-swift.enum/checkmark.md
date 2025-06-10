# UITableViewCell.AccessoryType.checkmark

**Framework**: UIKit  
**Kind**: case

A checkmark image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case checkmark
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Discussion

Choose this option to display a checkmark image. This type of accessory view doesn’t track touches.

To hide or show a check mark for a row, toggle the [`accessoryType`](uitableviewcell/accessorytype-swift.property.md) property of the cell between the [`UITableViewCell.AccessoryType.none`](uitableviewcell/accessorytype-swift.enum/none.md) and [`UITableViewCell.AccessoryType.checkmark`](uitableviewcell/accessorytype-swift.enum/checkmark.md) values. For example, if you use a checkmark to indicate one selected row from a group of rows, use your delegate’s [`tableView(_:didSelectRowAt:)`](uitableviewdelegate/tableview(_:didselectrowat:).md) method to update the accessory views of the affected rows.

## See Also

- [UITableViewCell.AccessoryType.none](uitableviewcell/accessorytype-swift.enum/none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.disclosureIndicator](uitableviewcell/accessorytype-swift.enum/disclosureindicator.md)
  A chevron-shaped control for presenting new content.
- [UITableViewCell.AccessoryType.detailDisclosureButton](uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton.md)
  An information button and a disclosure (chevron) control.
- [UITableViewCell.AccessoryType.detailButton](uitableviewcell/accessorytype-swift.enum/detailbutton.md)
  An information button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/checkmark)*