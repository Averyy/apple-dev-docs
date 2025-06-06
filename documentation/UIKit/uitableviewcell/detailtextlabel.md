# detailTextLabel

**Framework**: UIKit  
**Kind**: property

The secondary label of the table cell, if one exists.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var detailTextLabel: UILabel? { get }
```

## Mentions

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)

#### Discussion

Holds the secondary (or detail) label of the cell. `UITableViewCell` adds an appropriate label when you create the cell in a style that supports secondary labels. If the style doesn’t support detail labels, `nil` returns. See [`UITableViewCell.CellStyle`](uitableviewcell/cellstyle.md) for descriptions of the main label in currently defined cell styles.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](uitableviewcell/contentconfiguration-9ktox.md) resets this property to `nil`.

## See Also

- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](uitableviewcell/init(style:reuseidentifier:).md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
- [var textLabel: UILabel?](uitableviewcell/textlabel.md)
  The label to use for the main textual content of the table cell.
- [var imageView: UIImageView?](uitableviewcell/imageview.md)
  The image view of the table cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/detailtextlabel)*