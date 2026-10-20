# detailTextLabel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The secondary label of the table cell, if one exists.

**Availability**:
- iOS 3.0+ - Deprecated in 27.0
- iPadOS 3.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use a content configuration to manage the cell’s text instead. Use [`defaultContentConfiguration()`](./defaultcontentconfiguration%28%29.md) to get a default list content configuration, set your secondary text to the [`secondaryText`](../uilistcontentconfiguration-swift.struct/secondarytext.md) property of the configuration, and apply the configuration by setting it to the [`contentConfiguration`](./contentconfiguration-9ktox.md) property of the cell.

## Declaration

```swift
var detailTextLabel: UILabel? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UILabel * detailTextLabel;
```

## Mentions

- [Configuring the cells for your table](../configuring-the-cells-for-your-table.md)

#### Discussion

Holds the secondary (or detail) label of the cell. `UITableViewCell` adds an appropriate label when you create the cell in a style that supports secondary labels. If the style doesn’t support detail labels, `nil` returns. See [`UITableViewCell.CellStyle`](./cellstyle.md) for descriptions of the main label in currently defined cell styles.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](./contentconfiguration-9ktox.md) resets this property to `nil`.

## See Also

### Related Documentation
- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](./init%28style,reuseidentifier%29.md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
### Deprecated properties
- [var textLabel: UILabel?](./textlabel.md)
  The label to use for the main textual content of the table cell.
- [var imageView: UIImageView?](./imageview.md)
  The image view of the table cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/detailtextlabel)*