# tableView(_:heightForFooterInSection:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the height to use for the footer of a particular section.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, heightForFooterInSection section: Int) -> CGFloat
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)

#### Return Value

A nonnegative floating-point value that specifies the height (in points) of the footer for `section`.

#### Discussion

Use this method to specify the height of custom header views returned by your [`tableView(_:viewForFooterInSection:)`](uitableviewdelegate/tableview(_:viewforfooterinsection:).md) method.

## Parameters

- `tableView`: The table view requesting this information.
- `section`: An index number identifying a section of   .

## See Also

- [func tableView(UITableView, viewForFooterInSection: Int) -> UIView?](uitableviewdelegate/tableview(_:viewforfooterinsection:).md)
  Asks the delegate for a view to display in the footer of the specified section of the table view.
- [func tableView(UITableView, estimatedHeightForFooterInSection: Int) -> CGFloat](uitableviewdelegate/tableview(_:estimatedheightforfooterinsection:).md)
  Asks the delegate for the estimated height of the footer of a particular section.
- [func tableView(UITableView, heightForRowAt: IndexPath) -> CGFloat](uitableviewdelegate/tableview(_:heightforrowat:).md)
  Asks the delegate for the height to use for a row in a specified location.
- [func tableView(UITableView, heightForHeaderInSection: Int) -> CGFloat](uitableviewdelegate/tableview(_:heightforheaderinsection:).md)
  Asks the delegate for the height to use for the header of a particular section.
- [class let automaticDimension: CGFloat](uitableview/automaticdimension.md)
  A constant representing the default value for a given dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:heightforfooterinsection:))*