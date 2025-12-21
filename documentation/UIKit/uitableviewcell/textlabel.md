# textLabel

**Framework**: UIKit  
**Kind**: property

The label to use for the main textual content of the table cell.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textLabel: UILabel? { get }
```

## Mentions

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)
- [Filling a table with data](filling-a-table-with-data.md)

#### Discussion

This property holds the main label of the cell. [`UITableViewCell`](uitableviewcell.md) adds an appropriate label when you create the cell in a particular cell style. See [`UITableViewCell.CellStyle`](uitableviewcell/cellstyle.md) for descriptions of the main label in currently defined cell styles.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](uitableviewcell/contentconfiguration-9ktox.md) resets this property to `nil`.

## See Also

- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](uitableviewcell/init(style:reuseidentifier:).md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
- [var detailTextLabel: UILabel?](uitableviewcell/detailtextlabel.md)
  The secondary label of the table cell, if one exists.
- [var imageView: UIImageView?](uitableviewcell/imageview.md)
  The image view of the table cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/textlabel)*