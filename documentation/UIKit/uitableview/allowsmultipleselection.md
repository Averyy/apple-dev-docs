# allowsMultipleSelection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether users can select more than one row outside of editing mode.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var allowsMultipleSelection: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsMultipleSelection;
```

## Mentions

- [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md)

#### Discussion

This property controls whether a user can select multiple rows simultaneously outside of editing mode. Selected rows acquire a selected appearance.

In iOS, when the value of this property is [`true`](../../Swift/true.md), the user can select additional rows by tapping on them. The user must tap a currently selected row to deselect it.

In macOS, when the value of this property is [`true`](../../Swift/true.md), the user can select additional rows by holding the Command or Shift key while clicking on the additional rows they want to select. If the user isn’t holding a modifier key, clicking on another row clears the current selection and selects only the clicked row. This behavior resembles the selection behavior of [`NSTableView`](../../AppKit/nstableview.md).

If you access [`indexPathsForSelectedRows`](./indexpathsforselectedrows.md), you can get the index paths that identify the selected rows.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Selecting rows
- [var indexPathForSelectedRow: IndexPath?](./indexpathforselectedrow.md)
  An index path that identifies the row and section of the selected row.
- [var indexPathsForSelectedRows: [IndexPath]?](./indexpathsforselectedrows.md)
  The index paths that represent the selected rows.
- [func selectRow(at: IndexPath?, animated: Bool, scrollPosition: UITableView.ScrollPosition)](./selectrow%28at,animated,scrollposition%29.md)
  Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
- [func deselectRow(at: IndexPath, animated: Bool)](./deselectrow%28at,animated%29.md)
  Deselects a row that an index path identifies, with an option to animate the deselection.
- [var allowsSelection: Bool](./allowsselection.md)
  A Boolean value that determines whether users can select a row.
- [var allowsSelectionDuringEditing: Bool](./allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](./allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](./selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/allowsmultipleselection)*