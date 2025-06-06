# separatorInset

**Framework**: UIKit  
**Kind**: property

The inset values for the separator line drawn beneath the cell.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var separatorInset: UIEdgeInsets { get set }
```

#### Discussion

Use this property to indent the left and right edges of the separator line drawn beneath the cell. Positive inset values move the separator inward and away from edges of the cell. Negative values are treated as if the inset is set to 0.

The table view uses only the left and right inset values; it ignores the top and bottom inset values. The value assigned to this property takes precedence over any default separator insets set on the table view.

## See Also

- [var indentationLevel: Int](uitableviewcell/indentationlevel.md)
  The indentation level of the cell’s content.
- [var indentationWidth: CGFloat](uitableviewcell/indentationwidth.md)
  The width for each level of indentation of a cell’s content.
- [var shouldIndentWhileEditing: Bool](uitableviewcell/shouldindentwhileediting.md)
  A Boolean value that controls whether the cell background is indented when the table view is in editing mode.
- [UITableViewCell.SeparatorStyle](uitableviewcell/separatorstyle.md)
  The style for cells to use as separators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/separatorinset)*