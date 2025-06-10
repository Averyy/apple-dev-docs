# UITableViewCell.AccessoryType.disclosureIndicator

**Framework**: UIKit  
**Kind**: case

A chevron-shaped control for presenting new content.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case disclosureIndicator
```

#### Discussion

Choose this type when you want taps in the accessory view to display new content. Connect the accessory view itself to a push segue to display that content.

The table view doesn’t call the delegate’s [`tableView(_:accessoryButtonTappedForRowWith:)`](uitableviewdelegate/tableview(_:accessorybuttontappedforrowwith:).md) method in response to touch events in this accessory view.

## See Also

- [UITableViewCell.AccessoryType.none](uitableviewcell/accessorytype-swift.enum/none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.detailDisclosureButton](uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton.md)
  An information button and a disclosure (chevron) control.
- [UITableViewCell.AccessoryType.checkmark](uitableviewcell/accessorytype-swift.enum/checkmark.md)
  A checkmark image.
- [UITableViewCell.AccessoryType.detailButton](uitableviewcell/accessorytype-swift.enum/detailbutton.md)
  An information button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator)*