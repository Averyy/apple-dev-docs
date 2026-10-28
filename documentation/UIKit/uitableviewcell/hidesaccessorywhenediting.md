# hidesAccessoryWhenEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the accessory view is hidden when the cell is being edited.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`editingAccessoryType`](./editingaccessorytype.md) and [`editingAccessoryView`](./editingaccessoryview.md) properties instead.

## Declaration

```objc
@property (nonatomic) BOOL hidesAccessoryWhenEditing;
```

## Discussion

The default value is [`true`](../../Swift/true.md).

## See Also

### Deprecated properties
- [var textLabel: UILabel?](./textlabel.md)
  The label to use for the main textual content of the table cell.
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
- [target](./target.md)
  The target object to receive action messages.
- [editAction](./editaction.md)
  The selector defining the action message to invoke when users tap the insert or delete button.
- [accessoryAction](./accessoryaction.md)
  The selector defining the action message to invoke when users tap the accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/hidesaccessorywhenediting)*