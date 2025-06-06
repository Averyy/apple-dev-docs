# tableViewDidEndMultipleSelectionInteraction(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableViewDidEndMultipleSelectionInteraction(_ tableView: UITableView)
```

#### Discussion

The table view calls this method after the user lifts their finger from the device.

## Parameters

- `tableView`: The table view calling this method.

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
- [func tableView(UITableView, didDeselectRowAt: IndexPath)](uitableviewdelegate/tableview(_:diddeselectrowat:).md)
  Tells the delegate that the specified row is now deselected.
- [func tableView(UITableView, shouldBeginMultipleSelectionInteractionAt: IndexPath) -> Bool](uitableviewdelegate/tableview(_:shouldbeginmultipleselectioninteractionat:).md)
  Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.
- [func tableView(UITableView, didBeginMultipleSelectionInteractionAt: IndexPath)](uitableviewdelegate/tableview(_:didbeginmultipleselectioninteractionat:).md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableviewdidendmultipleselectioninteraction(_:))*