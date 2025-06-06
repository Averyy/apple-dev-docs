# indentationLevel

**Framework**: UIKit  
**Kind**: property

The indentation level of the cell’s content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var indentationLevel: Int { get set }
```

#### Discussion

The default value of the property is zero (no indentation). Assigning a positive value to this property indents the cell’s content from the left edge of the cell separator. The amount of indentation is equal to the indentation level multiplied by the value in the [`indentationWidth`](uitableviewcell/indentationwidth.md) property.

## See Also

- [var indentationWidth: CGFloat](uitableviewcell/indentationwidth.md)
  The width for each level of indentation of a cell’s content.
- [var shouldIndentWhileEditing: Bool](uitableviewcell/shouldindentwhileediting.md)
  A Boolean value that controls whether the cell background is indented when the table view is in editing mode.
- [var separatorInset: UIEdgeInsets](uitableviewcell/separatorinset.md)
  The inset values for the separator line drawn beneath the cell.
- [UITableViewCell.SeparatorStyle](uitableviewcell/separatorstyle.md)
  The style for cells to use as separators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/indentationlevel)*