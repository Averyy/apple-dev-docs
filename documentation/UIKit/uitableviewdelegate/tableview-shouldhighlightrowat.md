# tableView(_:shouldHighlightRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the specified row should be highlighted.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, shouldHighlightRowAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the row should be highlighted or [`false`](https://developer.apple.com/documentation/Swift/false) if it should not.

#### Discussion

As touch events arrive, the table view highlights rows in anticipation of the user selecting them. As it processes those touch events, the table view calls this method to ask your delegate if a given cell should be highlighted. Your delegate can implement this method and use it to prevent the highlighting of a row when another row is already selected or when other relevant criteria occur.

If you do not implement this method, the default return value is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `tableView`: The table view that is making this request.
- `indexPath`: The index path of the row being highlighted.

## See Also

- [func tableView(UITableView, didHighlightRowAt: IndexPath)](uitableviewdelegate/tableview(_:didhighlightrowat:).md)
  Tells the delegate that the specified row was highlighted.
- [func tableView(UITableView, didUnhighlightRowAt: IndexPath)](uitableviewdelegate/tableview(_:didunhighlightrowat:).md)
  Tells the delegate that the highlight was removed from the row at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldhighlightrowat:))*