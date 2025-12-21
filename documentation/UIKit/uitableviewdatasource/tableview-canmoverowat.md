# tableView(_:canMoveRowAt:)

**Framework**: UIKit  
**Kind**: method

Asks the data source whether a given row can move to another location in the table view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the row can be moved; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method allows the data source to specify that the reordering control for the specified row not be shown. By default, the reordering control is shown if the data source implements the [`tableView(_:moveRowAt:to:)`](uitableviewdatasource/tableview(_:moverowat:to:).md) method.

## Parameters

- `tableView`: The table-view object requesting this information.
- `indexPath`: An index path locating a row in  .

## See Also

- [func tableView(UITableView, moveRowAt: IndexPath, to: IndexPath)](uitableviewdatasource/tableview(_:moverowat:to:).md)
  Tells the data source to move a row at a specific location in the table view to another location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:canmoverowat:))*