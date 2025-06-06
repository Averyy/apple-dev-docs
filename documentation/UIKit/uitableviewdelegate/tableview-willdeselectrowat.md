# tableView(_:willDeselectRowAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that a specified row is about to be deselected.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, willDeselectRowAt indexPath: IndexPath) -> IndexPath?
```

#### Return Value

An index path that confirms or alters the deselected row. Return an `NSIndexPath` object other than `indexPath` if you want another cell to be deselected. Return `nil` if you don’t want the row deselected.

#### Discussion

This method is only called if there is an existing selection when the user tries to select a different row. The delegate is sent this method for the previously selected row. You can use [`UITableViewCell.SelectionStyle.none`](uitableviewcell/selectionstyle-swift.enum/none.md) to disable the appearance of the cell highlight on touch-down.

## Parameters

- `tableView`: A table view informing the delegate about the impending deselection.
- `indexPath`: An index path locating the row in   to be deselected.

## See Also

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)
  Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [func tableView(UITableView, willSelectRowAt: IndexPath) -> IndexPath?](uitableviewdelegate/tableview(_:willselectrowat:).md)
  Tells the delegate a row is about to be selected.
- [func tableView(UITableView, didSelectRowAt: IndexPath)](uitableviewdelegate/tableview(_:didselectrowat:).md)
  Tells the delegate a row is selected.
- [func tableView(UITableView, didDeselectRowAt: IndexPath)](uitableviewdelegate/tableview(_:diddeselectrowat:).md)
  Tells the delegate that the specified row is now deselected.
- [func tableView(UITableView, shouldBeginMultipleSelectionInteractionAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldbeginmultipleselectioninteractionat:).md)
  Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.
- [func tableView(UITableView, didBeginMultipleSelectionInteractionAt: IndexPath)](uitableviewdelegate/tableview(_:didbeginmultipleselectioninteractionat:).md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.
- [func tableViewDidEndMultipleSelectionInteraction(UITableView)](uitableviewdelegate/tableviewdidendmultipleselectioninteraction(_:).md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willdeselectrowat:))*