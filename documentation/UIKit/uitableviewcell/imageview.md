# imageView

**Framework**: UIKit  
**Kind**: property

The image view of the table cell.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var imageView: UIImageView? { get }
```

## Mentions

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)

#### Discussion

Returns the image view ([`UIImageView`](uiimageview.md) object) of the table view, which initially has no image set. If an image is set, it appears on the left side of the cell, before any label. `UITableViewCell` creates the image-view object when you create the cell.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](uitableviewcell/contentconfiguration-9ktox.md) resets this property to `nil`.

## See Also

- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](uitableviewcell/init(style:reuseidentifier:).md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
- [var textLabel: UILabel?](uitableviewcell/textlabel.md)
  The label to use for the main textual content of the table cell.
- [var detailTextLabel: UILabel?](uitableviewcell/detailtextlabel.md)
  The secondary label of the table cell, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/imageview)*