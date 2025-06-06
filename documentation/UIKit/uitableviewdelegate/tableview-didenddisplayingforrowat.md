# tableView(_:didEndDisplaying:forRowAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified cell was removed from the table.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, didEndDisplaying cell: UITableViewCell, forRowAt indexPath: IndexPath)
```

#### Discussion

Use this method to detect when a cell is removed from a table view, as opposed to monitoring the view itself to see when it appears or disappears.

## Parameters

- `tableView`: The table view that removed the view.
- `cell`: The cell that was removed.
- `indexPath`: The index path of the cell.

## See Also

- [func tableView(UITableView, didEndDisplayingHeaderView: UIView, forSection: Int)](uitableviewdelegate/tableview(_:didenddisplayingheaderview:forsection:).md)
  Tells the delegate that the specified header view was removed from the table.
- [func tableView(UITableView, didEndDisplayingFooterView: UIView, forSection: Int)](uitableviewdelegate/tableview(_:didenddisplayingfooterview:forsection:).md)
  Tells the delegate that the specified footer view was removed from the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didenddisplaying:forrowat:))*