# tableView(_:didHighlightRowAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified row was highlighted.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, didHighlightRowAt indexPath: IndexPath)
```

## Parameters

- `tableView`: The table view that highlighted the cell.
- `indexPath`: The index path of the row that was highlighted.

## See Also

- [func tableView(UITableView, shouldHighlightRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldhighlightrowat:).md)
  Asks the delegate if the specified row should be highlighted.
- [func tableView(UITableView, didUnhighlightRowAt: IndexPath)](uitableviewdelegate/tableview(_:didunhighlightrowat:).md)
  Tells the delegate that the highlight was removed from the row at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didhighlightrowat:))*