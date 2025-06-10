# UITableViewCell.SeparatorStyle

**Framework**: UIKit  
**Kind**: enum

The style for cells to use as separators.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum SeparatorStyle
```

#### Overview

You use these constants to set the value of the [`separatorStyle`](uitableview/separatorstyle.md) property defined by [`UITableView`](uitableview.md).

## Topics

### Constants
- [UITableViewCell.SeparatorStyle.none](uitableviewcell/separatorstyle/none.md)
  The separator cell has no distinct style.
- [UITableViewCell.SeparatorStyle.singleLine](uitableviewcell/separatorstyle/singleline.md)
  The separator cell has a single line running across its width.
- [UITableViewCell.SeparatorStyle.singleLineEtched](uitableviewcell/separatorstyle/singlelineetched.md)
  The separator cell has double lines running across its width, giving it an etched look.
### Initializers
- [init?(rawValue: Int)](uitableviewcell/separatorstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var separatorStyle: UITableViewCell.SeparatorStyle](uitableview/separatorstyle.md)
  The style for table cells to use as separators.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/separatorstyle)*