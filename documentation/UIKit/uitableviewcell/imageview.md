# imageView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image view of the table cell.

**Availability**:
- iOS 3.0+ - Deprecated in 27.0
- iPadOS 3.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use a content configuration to manage the cell’s image instead. Use [`defaultContentConfiguration()`](./defaultcontentconfiguration%28%29.md) to get a default list content configuration, set your image to the [`image`](../uilistcontentconfiguration-swift.struct/image.md) property of the configuration, and apply the configuration by setting it to the [`contentConfiguration`](./contentconfiguration-9ktox.md) property of the cell.

## Declaration

```swift
var imageView: UIImageView? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIImageView * imageView;
```

## Mentions

- [Configuring the cells for your table](../configuring-the-cells-for-your-table.md)

#### Discussion

Returns the image view ([`UIImageView`](../uiimageview.md) object) of the table view, which initially has no image set. If an image is set, it appears on the left side of the cell, before any label. `UITableViewCell` creates the image-view object when you create the cell.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](./contentconfiguration-9ktox.md) resets this property to `nil`.

## See Also

### Related Documentation
- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](./init%28style,reuseidentifier%29.md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
### Deprecated properties
- [var textLabel: UILabel?](./textlabel.md)
  The label to use for the main textual content of the table cell.
- [var detailTextLabel: UILabel?](./detailtextlabel.md)
  The secondary label of the table cell, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/imageview)*