# detailTextLabel

**Framework**: UIKit  
**Kind**: property

A detail text label for the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var detailTextLabel: UILabel? { get }
```

#### Discussion

This property is only for tables configured with [`UITableView.Style.grouped`](uitableview/style-swift.enum/grouped.md).

Accessing the value in this property causes the view to create a default label for displaying a detail text string. If you are managing the content of the view yourself by adding subviews to the [`contentView`](uitableviewheaderfooterview/contentview.md) property, you should not access this property.

The label sizes to fit the content view area in the best way possible according to the size of the string. Its size also adjusts depending on whether there is a primary text label present.

This property is mutually exclusive with a content configuration. Setting a non-`nil` value for [`contentConfiguration`](uitableviewheaderfooterview/contentconfiguration-6b4eg.md) resets this property to `nil`.

## See Also

- [func defaultContentConfiguration() -> UIListContentConfiguration](uitableviewheaderfooterview/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the view’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](uitableviewheaderfooterview/contentconfiguration-6b4eg.md)
  The current content configuration of the view.
- [var automaticallyUpdatesContentConfiguration: Bool](uitableviewheaderfooterview/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the view automatically updates its content configuration when its state changes.
- [var contentView: UIView](uitableviewheaderfooterview/contentview.md)
  The content view of the header or footer.
- [var textLabel: UILabel?](uitableviewheaderfooterview/textlabel.md)
  A primary text label for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/detailtextlabel)*