# UITableViewCell.AccessoryType.detailButton

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

An information button.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case detailButton
```

```c
UITableViewCellAccessoryDetailButton
```

#### Discussion

Choose this option to display a button that, when tapped, displays information about the row. Use your delegate’s [`tableView(_:accessoryButtonTappedForRowWith:)`](../../uitableviewdelegate/tableview%28_,accessorybuttontappedforrowwith%29.md) method to respond to taps in the button.

## See Also

### Accessory views
- [UITableViewCell.AccessoryType.none](./none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.disclosureIndicator](./disclosureindicator.md)
  A chevron-shaped control for presenting new content.
- [UITableViewCell.AccessoryType.detailDisclosureButton](./detaildisclosurebutton.md)
  An information button and a disclosure (chevron) control.
- [UITableViewCell.AccessoryType.checkmark](./checkmark.md)
  A checkmark image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/detailbutton)*