# UITableView.SeparatorInsetReference

**Framework**: UIKit  
**Kind**: enum

Constants that indicate how to interpret the separator inset value of a table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum SeparatorInsetReference
```

## Topics

### Constants
- [UITableView.SeparatorInsetReference.fromCellEdges](uitableview/separatorinsetreference-swift.enum/fromcelledges.md)
  An inset value that’s relative to the edge of the cell.
- [UITableView.SeparatorInsetReference.fromAutomaticInsets](uitableview/separatorinsetreference-swift.enum/fromautomaticinsets.md)
  An inset value that indicates the starting position is based on the default separator insets.
### Initializers
- [init?(rawValue: Int)](uitableview/separatorinsetreference-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [var separatorInsetReference: UITableView.SeparatorInsetReference](uitableview/separatorinsetreference-swift.property.md)
  An indicator of how to interpret the separator inset value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/separatorinsetreference-swift.enum)*