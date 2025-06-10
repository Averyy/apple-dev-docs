# UITableViewCell.AccessoryType.detailDisclosureButton

**Framework**: UIKit  
**Kind**: case

An information button and a disclosure (chevron) control.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
case detailDisclosureButton
```

#### Discussion

Choose this type when you want both an information button and a disclosure control. Connect the disclosure control to a push segue to display new content. Use the delegate’s [`tableView(_:accessoryButtonTappedForRowWith:)`](uitableviewdelegate/tableview(_:accessorybuttontappedforrowwith:).md)method to respond to touch events in the detail button.

## See Also

- [UITableViewCell.AccessoryType.none](uitableviewcell/accessorytype-swift.enum/none.md)
  No accessory view.
- [UITableViewCell.AccessoryType.disclosureIndicator](uitableviewcell/accessorytype-swift.enum/disclosureindicator.md)
  A chevron-shaped control for presenting new content.
- [UITableViewCell.AccessoryType.checkmark](uitableviewcell/accessorytype-swift.enum/checkmark.md)
  A checkmark image.
- [UITableViewCell.AccessoryType.detailButton](uitableviewcell/accessorytype-swift.enum/detailbutton.md)
  An information button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/detaildisclosurebutton)*