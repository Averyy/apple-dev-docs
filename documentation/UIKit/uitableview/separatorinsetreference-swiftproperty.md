# separatorInsetReference

**Framework**: UIKit  
**Kind**: property

An indicator of how to interpret the separator inset value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var separatorInsetReference: UITableView.SeparatorInsetReference { get set }
```

#### Discussion

Use the value of this property to determine how the value in the separatorInset property is interpreted for cells. The default value of this property is [`UITableView.SeparatorInsetReference.fromCellEdges`](uitableview/separatorinsetreference-swift.enum/fromcelledges.md).

## See Also

- [var separatorStyle: UITableViewCell.SeparatorStyle](uitableview/separatorstyle.md)
  The style for table cells to use as separators.
- [UITableViewCell.SeparatorStyle](uitableviewcell/separatorstyle.md)
  The style for cells to use as separators.
- [var separatorColor: UIColor?](uitableview/separatorcolor.md)
  The color of separator rows in the table view.
- [var separatorEffect: UIVisualEffect?](uitableview/separatoreffect.md)
  The effect to apply to table separators.
- [var separatorInset: UIEdgeInsets](uitableview/separatorinset.md)
  The default inset of cell separators.
- [UITableView.SeparatorInsetReference](uitableview/separatorinsetreference-swift.enum.md)
  Constants that indicate how to interpret the separator inset value of a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/separatorinsetreference-swift.property)*