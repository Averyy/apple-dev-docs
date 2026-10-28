# allowsSelection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether users can select a row.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var allowsSelection: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsSelection;
```

## Mentions

- [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md)

## Discussion

If the value of this property is [`true`](../../Swift/true.md) (the default), users can select rows. If you set it to [`false`](../../Swift/false.md), they can’t select rows. Setting this property affects cell selection only when the table view isn’t in editing mode. If you want to restrict selection of cells in editing mode, use [`allowsSelectionDuringEditing`](./allowsselectionduringediting.md).

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
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one row outside of editing mode.
- [var allowsSelectionDuringEditing: Bool](./allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](./allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](./selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/allowsselection)*