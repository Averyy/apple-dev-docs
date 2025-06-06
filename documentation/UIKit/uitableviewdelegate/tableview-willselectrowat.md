# tableView(_:willSelectRowAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate a row is about to be selected.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, willSelectRowAt indexPath: IndexPath) -> IndexPath?
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Return Value

An index path that confirms or alters the selected row. Return an [`IndexPath`](https://developer.apple.com/documentation/Foundation/IndexPath) (Swift) or [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) (Objective-C) other than `indexPath` if you want another cell to be selected. Return `nil` if you don’t want the row selected.

#### Discussion

The system calls this method after a user has lifted their finger; the row is highlighted on the initial touch, but only selected when the touch withdraws. You can use [`UITableViewCell.SelectionStyle.none`](uitableviewcell/selectionstyle-swift.enum/none.md) to disable the appearance of the cell highlight on the initial touch. The system doesn’t call this method if the rows in the table aren’t selectable. See [`Handling row selection in a table view`](handling-row-selection-in-a-table-view.md) for more information on controlling table row selection behavior.

## Parameters

- `tableView`: A table view informing the delegate about the impending selection.
- `indexPath`: An index path locating the row in  .

## See Also

- [func tableView(UITableView, shouldIndentWhileEditingRowAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldindentwhileeditingrowat:).md)
  Asks the delegate whether the background of the specified row should be indented while the table view is in editing mode.
- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)
  Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [func tableView(UITableView, didSelectRowAt: IndexPath)](uitableviewdelegate/tableview(_:didselectrowat:).md)
  Tells the delegate a row is selected.
- [func tableView(UITableView, willDeselectRowAt: IndexPath) -> IndexPath?](uitableviewdelegate/tableview(_:willdeselectrowat:).md)
  Tells the delegate that a specified row is about to be deselected.
- [func tableView(UITableView, didDeselectRowAt: IndexPath)](uitableviewdelegate/tableview(_:diddeselectrowat:).md)
  Tells the delegate that the specified row is now deselected.
- [func tableView(UITableView, shouldBeginMultipleSelectionInteractionAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldbeginmultipleselectioninteractionat:).md)
  Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.
- [func tableView(UITableView, didBeginMultipleSelectionInteractionAt: IndexPath)](uitableviewdelegate/tableview(_:didbeginmultipleselectioninteractionat:).md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.
- [func tableViewDidEndMultipleSelectionInteraction(UITableView)](uitableviewdelegate/tableviewdidendmultipleselectioninteraction(_:).md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willselectrowat:))*