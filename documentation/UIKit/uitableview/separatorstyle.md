# separatorStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style for table cells to use as separators.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var separatorStyle: UITableViewCell.SeparatorStyle { get set }
```

```objc
@property (nonatomic) UITableViewCellSeparatorStyle separatorStyle;
```

## Discussion

The value of this property is one of the separator-style constants described in [`UITableViewCell`](../uitableviewcell.md). `UITableView` uses this property to set the separator style on the cell returned from the delegate in [`tableView(_:cellForRowAt:)`](../uitableviewdatasource/tableview%28_,cellforrowat%29.md).

## See Also

### Customizing the separator appearance
- [UITableViewCell.SeparatorStyle](../uitableviewcell/separatorstyle.md)
  The style for cells to use as separators.
- [var separatorColor: UIColor?](./separatorcolor.md)
  The color of separator rows in the table view.
- [var separatorEffect: UIVisualEffect?](./separatoreffect.md)
  The effect to apply to table separators.
- [var separatorInset: UIEdgeInsets](./separatorinset.md)
  The default inset of cell separators.
- [var separatorInsetReference: UITableView.SeparatorInsetReference](./separatorinsetreference-swift.property.md)
  An indicator of how to interpret the separator inset value.
- [UITableView.SeparatorInsetReference](./separatorinsetreference-swift.enum.md)
  Constants that indicate how to interpret the separator inset value of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/separatorstyle)*