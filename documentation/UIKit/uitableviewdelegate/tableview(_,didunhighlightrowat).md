# tableView(_:didUnhighlightRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the highlight was removed from the row at the specified index path.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, didUnhighlightRowAt indexPath: IndexPath)
```

```objc
- (void) tableView:(UITableView *) tableView didUnhighlightRowAtIndexPath:(NSIndexPath *) indexPath;
```

## Parameters

- `tableView`: The table view that removed the highlight from the cell.
- `indexPath`: The index path of the row that had its highlight removed.

## See Also

### Managing table view highlights
- [func tableView(UITableView, shouldHighlightRowAt: IndexPath) -> Bool](./tableview%28_,shouldhighlightrowat%29.md)
  Asks the delegate if the specified row should be highlighted.
- [func tableView(UITableView, didHighlightRowAt: IndexPath)](./tableview%28_,didhighlightrowat%29.md)
  Tells the delegate that the specified row was highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:didunhighlightrowat:))*