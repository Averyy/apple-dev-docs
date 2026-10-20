# UITableView.SeparatorInsetReference

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UITableViewSeparatorInsetReference : NSInteger;
```

## Topics

### Constants
- [UITableView.SeparatorInsetReference.fromCellEdges](./separatorinsetreference-swift.enum/fromcelledges.md)
  An inset value that’s relative to the edge of the cell.
- [UITableView.SeparatorInsetReference.fromAutomaticInsets](./separatorinsetreference-swift.enum/fromautomaticinsets.md)
  An inset value that indicates the starting position is based on the default separator insets.
### Initializers
- [init?(rawValue: Int)](./separatorinsetreference-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing the separator appearance
- [var separatorStyle: UITableViewCell.SeparatorStyle](./separatorstyle.md)
  The style for table cells to use as separators.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/separatorinsetreference-swift.enum)*