# indexPathsForSelectedRows

**Framework**: UIKit  
**Kind**: property

The index paths that represent the selected rows.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var indexPathsForSelectedRows: [IndexPath]? { get }
```

#### Discussion

The value of this property is an array of index-path objects each identifying a row through its section and row index. The value of this property is `nil` if there are no selected rows.

## See Also

- [var indexPathForSelectedRow: IndexPath?](uitableview/indexpathforselectedrow.md)
  An index path that identifies the row and section of the selected row.
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
- [var allowsMultipleSelectionDuringEditing: Bool](uitableview/allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](uitableview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [class let selectionDidChangeNotification: NSNotification.Name](uitableview/selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/indexpathsforselectedrows)*