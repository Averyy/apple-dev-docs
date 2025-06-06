# tableView(_:estimatedHeightForRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the estimated height of a row in a specified location.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, estimatedHeightForRowAt indexPath: IndexPath) -> CGFloat
```

## Mentions

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md)

#### Return Value

A nonnegative floating-point value that estimates the height (in points) that `row` should be. Return [`automaticDimension`](uitableview/automaticdimension.md) if you have no estimate.

#### Discussion

Providing an estimate the height of rows can improve the user experience when loading the table view. If the table contains variable height rows, it might be expensive to calculate all their heights and so lead to a longer load time. Using estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

## Parameters

- `tableView`: The table view requesting this information.
- `indexPath`: An index path that locates a row in  .

## See Also

- [func tableView(UITableView, heightForRowAt: IndexPath) -> CGFloat](uitableviewdelegate/tableview(_:heightforrowat:).md)
  Asks the delegate for the height to use for a row in a specified location.
- [func tableView(UITableView, estimatedHeightForHeaderInSection: Int) -> CGFloat](uitableviewdelegate/tableview(_:estimatedheightforheaderinsection:).md)
  Asks the delegate for the estimated height of the header of a particular section.
- [func tableView(UITableView, estimatedHeightForFooterInSection: Int) -> CGFloat](uitableviewdelegate/tableview(_:estimatedheightforfooterinsection:).md)
  Asks the delegate for the estimated height of the footer of a particular section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforrowat:))*