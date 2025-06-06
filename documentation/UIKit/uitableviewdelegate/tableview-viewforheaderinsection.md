# tableView(_:viewForHeaderInSection:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a view to display in the header of the specified section of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView?
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)

#### Return Value

A [`UILabel`](uilabel.md), [`UIImageView`](uiimageview.md), or custom view to display at the top of the specified section.

#### Discussion

If you implement this method but don’t implement [`tableView(_:heightForHeaderInSection:)`](uitableviewdelegate/tableview(_:heightforheaderinsection:).md), the table view calculates the height automatically, or uses the value of [`sectionHeaderHeight`](uitableview/sectionheaderheight.md) if set.

## Parameters

- `tableView`: The table view asking for the view.
- `section`: The index number of the section containing the header view.

## See Also

- [func tableView(UITableView, viewForFooterInSection: Int) -> UIView?](uitableviewdelegate/tableview(_:viewforfooterinsection:).md)
  Asks the delegate for a view to display in the footer of the specified section of the table view.
- [func tableView(UITableView, willDisplayHeaderView: UIView, forSection: Int)](uitableviewdelegate/tableview(_:willdisplayheaderview:forsection:).md)
  Tells the delegate that the table is about to display the header view for the specified section.
- [func tableView(UITableView, willDisplayFooterView: UIView, forSection: Int)](uitableviewdelegate/tableview(_:willdisplayfooterview:forsection:).md)
  Tells the delegate that the table is about to display the footer view for the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:viewforheaderinsection:))*