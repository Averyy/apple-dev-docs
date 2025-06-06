# tableView(_:estimatedHeightForHeaderInSection:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the estimated height of the header of a particular section.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, estimatedHeightForHeaderInSection section: Int) -> CGFloat
```

## Mentions

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md)

#### Return Value

A nonnegative floating-point value that specifies the height (in points) of the header for `section`.

#### Discussion

Providing an estimate the height of section headers can improve the user experience when loading the table view. If the table contains variable height section headers, it might be expensive to calculate all their heights and so lead to a longer load time. Using estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

## Parameters

- `tableView`: The table view requesting this information.
- `section`: An index number identifying a section of   .

## See Also

- [func tableView(UITableView, heightForHeaderInSection: Int) -> CGFloat](uitableviewdelegate/tableview(_:heightforheaderinsection:).md)
  Asks the delegate for the height to use for the header of a particular section.
- [func tableView(UITableView, estimatedHeightForRowAt: IndexPath) -> CGFloat](uitableviewdelegate/tableview(_:estimatedheightforrowat:).md)
  Asks the delegate for the estimated height of a row in a specified location.
- [func tableView(UITableView, estimatedHeightForFooterInSection: Int) -> CGFloat](uitableviewdelegate/tableview(_:estimatedheightforfooterinsection:).md)
  Asks the delegate for the estimated height of the footer of a particular section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforheaderinsection:))*