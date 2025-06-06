# allowsMultipleSelectionDuringEditing

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsMultipleSelectionDuringEditing: Bool { get set }
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). If you set it to [`true`](https://developer.apple.com/documentation/swift/true), check marks appear next to selected rows in editing mode. In addition, [`UITableView`](uitableview.md) doesn’t query for editing styles when it goes into editing mode. If you access [`indexPathsForSelectedRows`](uitableview/indexpathsforselectedrows.md), you can get the index paths that identify the selected rows.

## See Also

- [var indexPathForSelectedRow: IndexPath?](uitableview/indexpathforselectedrow.md)
  An index path that identifies the row and section of the selected row.
- [var indexPathsForSelectedRows: [IndexPath]?](uitableview/indexpathsforselectedrows.md)
  The index paths that represent the selected rows.
- [func selectRow(at: IndexPath?, animated: Bool, scrollPosition: UITableView.ScrollPosition)](uitableview/selectrow(at:animated:scrollposition:).md)
  Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
- [func deselectRow(at: IndexPath, animated: Bool)](uitableview/deselectrow(at:animated:).md)
  Deselects a row that an index path identifies, with an option to animate the deselection.
- [var allowsSelection: Bool](uitableview/allowsselection.md)
  A Boolean value that determines whether users can select a row.
- [var allowsMultipleSelection: Bool](uitableview/allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one row outside of editing mode.
- [var allowsSelectionDuringEditing: Bool](uitableview/allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [var selectionFollowsFocus: Bool](uitableview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [class let selectionDidChangeNotification: NSNotification.Name](uitableview/selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/allowsmultipleselectionduringediting)*