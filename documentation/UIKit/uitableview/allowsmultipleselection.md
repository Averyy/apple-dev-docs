# allowsMultipleSelection

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether users can select more than one row outside of editing mode.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsMultipleSelection: Bool { get set }
```

## Mentions

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Discussion

This property controls whether a user can select multiple rows simultaneously outside of editing mode. Selected rows acquire a selected appearance.

In iOS, when the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the user can select additional rows by tapping on them. The user must tap a currently selected row to deselect it.

In macOS, when the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the user can select additional rows by holding the Command or Shift key while clicking on the additional rows they want to select. If the user isn’t holding a modifier key, clicking on another row clears the current selection and selects only the clicked row. This behavior resembles the selection behavior of [`NSTableView`](https://developer.apple.com/documentation/AppKit/NSTableView).

If you access [`indexPathsForSelectedRows`](uitableview/indexpathsforselectedrows.md), you can get the index paths that identify the selected rows.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

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
- [var allowsSelectionDuringEditing: Bool](uitableview/allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](uitableview/allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](uitableview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [class let selectionDidChangeNotification: NSNotification.Name](uitableview/selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/allowsmultipleselection)*