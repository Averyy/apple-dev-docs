# UITableViewCell.AccessoryType.checkmark

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A checkmark image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
case checkmark
```

```c
UITableViewCellAccessoryCheckmark
```

## Mentions

- [Handling row selection in a table view](../../handling-row-selection-in-a-table-view.md)

## Discussion

Choose this option to display a checkmark image. This type of accessory view doesn’t track touches.

To hide or show a check mark for a row, toggle the [`accessoryType`](../accessorytype-swift.property.md) property of the cell between the [`UITableViewCell.AccessoryType.none`](./none.md) and [`UITableViewCell.AccessoryType.checkmark`](./checkmark.md) values. For example, if you use a checkmark to indicate one selected row from a group of rows, use your delegate’s [`tableView(_:didSelectRowAt:)`](../../uitableviewdelegate/tableview%28_,didselectrowat%29.md) method to update the accessory views of the affected rows.

## See Also

### Accessory views
- [UITableViewCell.AccessoryType.none](./none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.disclosureIndicator](./disclosureindicator.md)
  A chevron-shaped control for presenting new content.
- [UITableViewCell.AccessoryType.detailDisclosureButton](./detaildisclosurebutton.md)
  An information button and a disclosure (chevron) control.
- [UITableViewCell.AccessoryType.detailButton](./detailbutton.md)
  An information button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/checkmark)*