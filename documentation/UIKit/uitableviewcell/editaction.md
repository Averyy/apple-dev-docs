# editAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The selector defining the action message to invoke when users tap the insert or delete button.

**Availability**:
- iOS 2.0+ - Deprecated in 3.0
- iPadOS 2.0+ - Deprecated in 3.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Instead, use [`tableView(_:commit:forRowAt:)`](../uitableviewdatasource/tableview%28_,commit,forrowat%29.md) or [`tableView(_:accessoryButtonTappedForRowWith:)`](../uitableviewdelegate/tableview%28_,accessorybuttontappedforrowwith%29.md) for handling taps on cells.

## Declaration

```objc
@property (nonatomic, nullable) SEL editAction;
```

#### Discussion

When the cell’s table is in editing mode, the cell displays a green insert control or a red delete control to the left of it. (The [`selectedBackgroundView`](./selectedbackgroundview.md) constant applied to the cell via the [`editingStyle`](./editingstyle-swift.property.md) property determines which control is used.) Typically, the associated [`UITableView`](../uitableview.md) object sets the editing action for all cells; you can use this property to alter the editing action for individual cells. If the value of this property is `NULL`, no action message is sent.

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
- [hidesAccessoryWhenEditing](./hidesaccessorywhenediting.md)
  A Boolean value that determines whether the accessory view is hidden when the cell is being edited.
- [target](./target.md)
  The target object to receive action messages.
- [accessoryAction](./accessoryaction.md)
  The selector defining the action message to invoke when users tap the accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/editaction)*