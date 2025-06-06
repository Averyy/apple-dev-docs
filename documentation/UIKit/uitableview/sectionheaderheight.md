# sectionHeaderHeight

**Framework**: UIKit  
**Kind**: property

The height of section headers in the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sectionHeaderHeight: CGFloat { get set }
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)

#### Discussion

The default value is [`automaticDimension`](uitableview/automaticdimension.md). If the delegate doesn’t implement [`tableView(_:heightForHeaderInSection:)`](uitableviewdelegate/tableview(_:heightforheaderinsection:).md), the table view calculates the height automatically. To override automatic height calculation, set this property to a positive value.

## See Also

- [var tableHeaderView: UIView?](uitableview/tableheaderview.md)
  The view that displays above the table’s content.
- [var sectionFooterHeight: CGFloat](uitableview/sectionfooterheight.md)
  The height of section footers in the table view.
- [var estimatedSectionHeaderHeight: CGFloat](uitableview/estimatedsectionheaderheight.md)
  The estimated height of section headers in the table view.
- [var estimatedSectionFooterHeight: CGFloat](uitableview/estimatedsectionfooterheight.md)
  The estimated height of section footers in the table view.
- [var sectionHeaderTopPadding: CGFloat](uitableview/sectionheadertoppadding.md)
  The amount of padding above each section header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/sectionheaderheight)*