# tableView(_:didDeselectRowAt:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the specified row is now deselected.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, didDeselectRowAt indexPath: IndexPath)
```

#### Discussion

The delegate handles row deselections in this method. It could, for example, remove the check-mark image ([`UITableViewCell.AccessoryType.checkmark`](uitableviewcell/accessorytype-swift.enum/checkmark.md)) associated with the row.

## Parameters

- `tableView`: A table view informing the delegate about the row deselection.
- `indexPath`: An index path locating the deselected row in  .

## See Also

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)
  Detect when a user taps a table view cell so your app can take the next indicated action.
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [func tableView(UITableView, willSelectRowAt: IndexPath) -> IndexPath?](uitableviewdelegate/tableview(_:willselectrowat:).md)
  Tells the delegate a row is about to be selected.
- [func tableView(UITableView, didSelectRowAt: IndexPath)](uitableviewdelegate/tableview(_:didselectrowat:).md)
  Tells the delegate a row is selected.
- [func tableView(UITableView, willDeselectRowAt: IndexPath) -> IndexPath?](uitableviewdelegate/tableview(_:willdeselectrowat:).md)
  Tells the delegate that a specified row is about to be deselected.
- [func tableView(UITableView, shouldBeginMultipleSelectionInteractionAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldbeginmultipleselectioninteractionat:).md)
  Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.
- [func tableView(UITableView, didBeginMultipleSelectionInteractionAt: IndexPath)](uitableviewdelegate/tableview(_:didbeginmultipleselectioninteractionat:).md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.
- [func tableViewDidEndMultipleSelectionInteraction(UITableView)](uitableviewdelegate/tableviewdidendmultipleselectioninteraction(_:).md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:diddeselectrowat:))*