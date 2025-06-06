# tableView(_:willDisplayFooterView:forSection:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the table is about to display the footer view for the specified section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, willDisplayFooterView view: UIView, forSection section: Int)
```

## Parameters

- `tableView`: The table view informing the delegate of this event.
- `view`: The footer view that is about to be displayed.
- `section`: The index number of the section containing the footer view.

## See Also

- [func tableView(UITableView, viewForHeaderInSection: Int) -> UIView?](uitableviewdelegate/tableview(_:viewforheaderinsection:).md)
  Asks the delegate for a view to display in the header of the specified section of the table view.
- [func tableView(UITableView, viewForFooterInSection: Int) -> UIView?](uitableviewdelegate/tableview(_:viewforfooterinsection:).md)
  Asks the delegate for a view to display in the footer of the specified section of the table view.
- [func tableView(UITableView, willDisplayHeaderView: UIView, forSection: Int)](uitableviewdelegate/tableview(_:willdisplayheaderview:forsection:).md)
  Tells the delegate that the table is about to display the header view for the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willdisplayfooterview:forsection:))*