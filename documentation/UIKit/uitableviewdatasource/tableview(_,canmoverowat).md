# tableView(_:canMoveRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the data source whether a given row can move to another location in the table view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) tableView:(UITableView *) tableView canMoveRowAtIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

[`true`](../../Swift/true.md) if the row can be moved; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method allows the data source to specify that the reordering control for the specified row not be shown. By default, the reordering control is shown if the data source implements the [`tableView(_:moveRowAt:to:)`](./tableview%28_,moverowat,to%29.md) method.

## Parameters

- `tableView`: The table-view object requesting this information.
- `indexPath`: An index path locating a row in `tableView`.

## See Also

### Reordering table rows
- [func tableView(UITableView, moveRowAt: IndexPath, to: IndexPath)](./tableview%28_,moverowat,to%29.md)
  Tells the data source to move a row at a specific location in the table view to another location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:canmoverowat:))*