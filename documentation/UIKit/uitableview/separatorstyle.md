# separatorStyle

**Framework**: UIKit  
**Kind**: property

The style for table cells to use as separators.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var separatorStyle: UITableViewCell.SeparatorStyle { get set }
```

#### Discussion

The value of this property is one of the separator-style constants described in [`UITableViewCell`](uitableviewcell.md). `UITableView` uses this property to set the separator style on the cell returned from the delegate in [`tableView(_:cellForRowAt:)`](uitableviewdatasource/tableview(_:cellforrowat:).md).

## See Also

- [UITableViewCell.SeparatorStyle](uitableviewcell/separatorstyle.md)
  The style for cells to use as separators.
- [var separatorColor: UIColor?](uitableview/separatorcolor.md)
  The color of separator rows in the table view.
- [var separatorEffect: UIVisualEffect?](uitableview/separatoreffect.md)
  The effect to apply to table separators.
- [var separatorInset: UIEdgeInsets](uitableview/separatorinset.md)
  The default inset of cell separators.
- [var separatorInsetReference: UITableView.SeparatorInsetReference](uitableview/separatorinsetreference-swift.property.md)
  An indicator of how to interpret the separator inset value.
- [UITableView.SeparatorInsetReference](uitableview/separatorinsetreference-swift.enum.md)
  Constants that indicate how to interpret the separator inset value of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/separatorstyle)*