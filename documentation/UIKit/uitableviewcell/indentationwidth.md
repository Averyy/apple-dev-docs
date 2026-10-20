# indentationWidth

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The width for each level of indentation of a cell’s content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var indentationWidth: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat indentationWidth;
```

#### Discussion

The default indentation width is `10.0` points.

## See Also

### Managing content indentation
- [var indentationLevel: Int](./indentationlevel.md)
  The indentation level of the cell’s content.
- [var shouldIndentWhileEditing: Bool](./shouldindentwhileediting.md)
  A Boolean value that controls whether the cell background is indented when the table view is in editing mode.
- [var separatorInset: UIEdgeInsets](./separatorinset.md)
  The inset values for the separator line drawn beneath the cell.
- [UITableViewCell.SeparatorStyle](./separatorstyle.md)
  The style for cells to use as separators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/indentationwidth)*