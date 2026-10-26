# textLabel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The label to use for the main textual content of the table cell.

**Availability**:
- iOS 3.0+ - Deprecated in 27.0
- iPadOS 3.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use a content configuration to manage the cell’s text instead. Use [`defaultContentConfiguration()`](./defaultcontentconfiguration%28%29.md) to get a default list content configuration, set your primary text to the [`text`](../uilistcontentconfiguration-swift.struct/text.md) property of the configuration, and apply the configuration by setting it to the [`contentConfiguration`](./contentconfiguration-9ktox.md) property of the cell.

## Declaration

```swift
var textLabel: UILabel? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UILabel * textLabel;
```

## Mentions

- [Configuring the cells for your table](../configuring-the-cells-for-your-table.md)
- [Filling a table with data](../filling-a-table-with-data.md)

#### Discussion

This property holds the main label of the cell. [`UITableViewCell`](../uitableviewcell.md) adds an appropriate label when you create the cell in a particular cell style. See [`UITableViewCell.CellStyle`](./cellstyle.md) for descriptions of the main label in currently defined cell styles.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](./contentconfiguration-9ktox.md) resets this property to `nil`.

## See Also

### Related Documentation
- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](./init%28style,reuseidentifier%29.md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
### Deprecated properties
- [var detailTextLabel: UILabel?](./detailtextlabel.md)
  The secondary label of the table cell, if one exists.
- [var imageView: UIImageView?](./imageview.md)
  The image view of the table cell.
- [text](./text.md)
  The text of the cell.
- [font](./font.md)
  The font of the title.
- [textAlignment](./textalignment.md)
  A constant that specifies the alignment of text in the cell.
- [textColor](./textcolor.md)
  The color of the title text.
- [selectedTextColor](./selectedtextcolor.md)
  The color of the title text when the cell is selected.
- [lineBreakMode](./linebreakmode.md)
  The mode for wrapping and truncating text in the cell.
- [image](./image.md)
  The image to use as content for the cell.
- [selectedImage](./selectedimage.md)
  The image to use a cell content when the cell is selected.
- [hidesAccessoryWhenEditing](./hidesaccessorywhenediting.md)
  A Boolean value that determines whether the accessory view is hidden when the cell is being edited.
- [target](./target.md)
  The target object to receive action messages.
- [editAction](./editaction.md)
  The selector defining the action message to invoke when users tap the insert or delete button.
- [accessoryAction](./accessoryaction.md)
  The selector defining the action message to invoke when users tap the accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/textlabel)*