# tableHeaderView

**Framework**: UIKit  
**Kind**: property

The view that displays above the table’s content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tableHeaderView: UIView? { get set }
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)

#### Discussion

Use this property to specify a header view for your entire table. The header view is the first item to appear in the table’s view’s scrolling content, and it’s separate from the header views you add to individual sections. The default value of this property is `nil`.

When assigning a view to this property, set the height of that view to a nonzero value. The table view respects only the height of your view’s frame rectangle; it adjusts the width of your header view automatically to match the table view’s width.

## See Also

- [var sectionHeaderHeight: CGFloat](uitableview/sectionheaderheight.md)
  The height of section headers in the table view.
- [var style: UITableView.Style](uitableview/style-swift.property.md)
  The style of the table view.
- [UITableView.Style](uitableview/style-swift.enum.md)
  Constants for the table view styles.
- [var tableFooterView: UIView?](uitableview/tablefooterview.md)
  The view that displays below the table’s content.
- [var backgroundView: UIView?](uitableview/backgroundview.md)
  The background view of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/tableheaderview)*