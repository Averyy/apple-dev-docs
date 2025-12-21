# tableView(_:shouldBeginMultipleSelectionInteractionAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the user can use a two-finger pan gesture to select multiple items in a table view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, shouldBeginMultipleSelectionInteractionAt indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the user to select multiple rows using a two-finger pan gesture; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) to disable the behavior. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When the system recognizes a two-finger pan gesture, it calls this method before it sets [`isEditing`](uitableview/isediting.md) to [`true`](https://developer.apple.com/documentation/Swift/true). If you return [`true`](https://developer.apple.com/documentation/Swift/true) from this method, the user can select multiple rows using a two-finger pan gesture.

In macOS, the system calls this method when a user attempts to select multiple rows by holding a modifier key and clicking additional rows to select them.

To support multiple selection using the two-finger pan gesture (in iOS) or modifier keys (in macOS), set the [`allowsMultipleSelectionDuringEditing`](uitableview/allowsmultipleselectionduringediting.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) when you configure the table view.

## Parameters

- `tableView`: The table view calling this method.
- `indexPath`: The index path of the row that the user touched to start the two-finger pan gesture.

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
- [func tableView(UITableView, didBeginMultipleSelectionInteractionAt: IndexPath)](uitableviewdelegate/tableview(_:didbeginmultipleselectioninteractionat:).md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple rows in a table view.
- [func tableViewDidEndMultipleSelectionInteraction(UITableView)](uitableviewdelegate/tableviewdidendmultipleselectioninteraction(_:).md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple rows in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:shouldbeginmultipleselectioninteractionat:))*