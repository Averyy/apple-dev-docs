# UITableViewCell.AccessoryType.disclosureIndicator

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A chevron-shaped control for presenting new content.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
case disclosureIndicator
```

```c
UITableViewCellAccessoryDisclosureIndicator
```

#### Discussion

Choose this type when you want taps in the accessory view to display new content. Connect the accessory view itself to a push segue to display that content.

The table view doesn’t call the delegate’s [`tableView(_:accessoryButtonTappedForRowWith:)`](../../uitableviewdelegate/tableview%28_,accessorybuttontappedforrowwith%29.md) method in response to touch events in this accessory view.

## See Also

### Accessory views
- [UITableViewCell.AccessoryType.none](./none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.detailDisclosureButton](./detaildisclosurebutton.md)
  An information button and a disclosure (chevron) control.
- [UITableViewCell.AccessoryType.checkmark](./checkmark.md)
  A checkmark image.
- [UITableViewCell.AccessoryType.detailButton](./detailbutton.md)
  An information button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator)*