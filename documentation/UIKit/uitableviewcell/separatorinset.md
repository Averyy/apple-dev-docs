# separatorInset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The inset values for the separator line drawn beneath the cell.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var separatorInset: UIEdgeInsets { get set }
```

```objc
@property (nonatomic) UIEdgeInsets separatorInset;
```

## Discussion

Use this property to indent the left and right edges of the separator line drawn beneath the cell. Positive inset values move the separator inward and away from edges of the cell. Negative values are treated as if the inset is set to 0.

The table view uses only the left and right inset values; it ignores the top and bottom inset values. The value assigned to this property takes precedence over any default separator insets set on the table view.

## See Also

### Managing content indentation
- [var indentationLevel: Int](./indentationlevel.md)
  The indentation level of the cell’s content.
- [var indentationWidth: CGFloat](./indentationwidth.md)
  The width for each level of indentation of a cell’s content.
- [var shouldIndentWhileEditing: Bool](./shouldindentwhileediting.md)
  A Boolean value that controls whether the cell background is indented when the table view is in editing mode.
- [UITableViewCell.SeparatorStyle](./separatorstyle.md)
  The style for cells to use as separators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/separatorinset)*