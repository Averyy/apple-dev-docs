# shouldIndentWhileEditing

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether the cell background is indented when the table view is in editing mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shouldIndentWhileEditing: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). This property is unrelated to [`indentationLevel`](uitableviewcell/indentationlevel.md). The delegate can override this value in [`tableView(_:shouldIndentWhileEditingRowAt:)`](uitableviewdelegate/tableview(_:shouldindentwhileeditingrowat:).md). This property has an effect only on table views created in the grouped style ([`UITableView.Style.grouped`](uitableview/style-swift.enum/grouped.md)); it has no effect on [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md) table views.

## See Also

- [var indentationLevel: Int](uitableviewcell/indentationlevel.md)
  The indentation level of the cell’s content.
- [var indentationWidth: CGFloat](uitableviewcell/indentationwidth.md)
  The width for each level of indentation of a cell’s content.
- [var separatorInset: UIEdgeInsets](uitableviewcell/separatorinset.md)
  The inset values for the separator line drawn beneath the cell.
- [UITableViewCell.SeparatorStyle](uitableviewcell/separatorstyle.md)
  The style for cells to use as separators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/shouldindentwhileediting)*