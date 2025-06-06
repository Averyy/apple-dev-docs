# selectRow(at:animated:scrollPosition:)

**Framework**: UIKit  
**Kind**: method

Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func selectRow(at indexPath: IndexPath?, animated: Bool, scrollPosition: UITableView.ScrollPosition)
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Discussion

Calling this method doesn’t cause the delegate to receive a [`tableView(_:willSelectRowAt:)`](uitableviewdelegate/tableview(_:willselectrowat:).md) or [`tableView(_:didSelectRowAt:)`](uitableviewdelegate/tableview(_:didselectrowat:).md) message, nor does it send [`selectionDidChangeNotification`](uitableview/selectiondidchangenotification.md) notifications to observers.

##### Special Considerations

Passing [`UITableView.ScrollPosition.none`](uitableview/scrollposition/none.md) results in no scrolling, rather than the minimum scrolling described for that constant. To scroll to the newly selected row with minimum scrolling, select the row using this method with [`UITableView.ScrollPosition.none`](uitableview/scrollposition/none.md), then call [`scrollToRow(at:at:animated:)`](uitableview/scrolltorow(at:at:animated:).md) with [`UITableView.ScrollPosition.none`](uitableview/scrollposition/none.md).

```objc
NSIndexPath *rowToSelect;  // assume this exists and is set properly
UITableView *myTableView;  // assume this exists
 
[myTableView selectRowAtIndexPath:rowToSelect animated:YES scrollPosition:UITableViewScrollPositionNone];
[myTableView scrollToRowAtIndexPath:rowToSelect atScrollPosition:UITableViewScrollPositionNone animated:YES];
```

## Parameters

- `indexPath`: An index path identifying a row in the table view.
- `animated`:   if you want to animate the selection and any change in position;   if the change should be immediate.
- `scrollPosition`: A constant that identifies a relative position in the table view (top, middle, bottom) for the row when scrolling concludes. See   for descriptions of valid constants.

## See Also

- [var indexPathForSelectedRow: IndexPath?](uitableview/indexpathforselectedrow.md)
  An index path that identifies the row and section of the selected row.
- [var indexPathsForSelectedRows: [IndexPath]?](uitableview/indexpathsforselectedrows.md)
  The index paths that represent the selected rows.
- [func deselectRow(at: IndexPath, animated: Bool)](uitableview/deselectrow(at:animated:).md)
  Deselects a row that an index path identifies, with an option to animate the deselection.
- [var allowsSelection: Bool](uitableview/allowsselection.md)
  A Boolean value that determines whether users can select a row.
- [var allowsMultipleSelection: Bool](uitableview/allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one row outside of editing mode.
- [var allowsSelectionDuringEditing: Bool](uitableview/allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](uitableview/allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](uitableview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [class let selectionDidChangeNotification: NSNotification.Name](uitableview/selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/selectrow(at:animated:scrollposition:))*