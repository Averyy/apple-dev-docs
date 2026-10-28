# UITableViewCell.AccessoryType.detailDisclosureButton

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

An information button and a disclosure (chevron) control.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
case detailDisclosureButton
```

```c
UITableViewCellAccessoryDetailDisclosureButton
```

## Discussion

Choose this type when you want both an information button and a disclosure control. Connect the disclosure control to a push segue to display new content. Use the delegate’s [`tableView(_:accessoryButtonTappedForRowWith:)`](../../uitableviewdelegate/tableview%28_,accessorybuttontappedforrowwith%29.md)method to respond to touch events in the detail button.

## See Also

### Accessory views
- [UITableViewCell.AccessoryType.none](./none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.disclosureIndicator](./disclosureindicator.md)
  A chevron-shaped control for presenting new content.
- [UITableViewCell.AccessoryType.checkmark](./checkmark.md)
  A checkmark image.
- [UITableViewCell.AccessoryType.detailButton](./detailbutton.md)
  An information button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton)*