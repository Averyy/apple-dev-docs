# allowsMultipleSelectionDuringEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var allowsMultipleSelectionDuringEditing: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsMultipleSelectionDuringEditing;
```

## Mentions

- [Handling row selection in a table view](../handling-row-selection-in-a-table-view.md)

#### Discussion

The default value of this property is [`false`](../../Swift/false.md). If you set it to [`true`](../../Swift/true.md), check marks appear next to selected rows in editing mode. In addition, [`UITableView`](../uitableview.md) doesn’t query for editing styles when it goes into editing mode. If you access [`indexPathsForSelectedRows`](./indexpathsforselectedrows.md), you can get the index paths that identify the selected rows.

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
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one row outside of editing mode.
- [var allowsSelectionDuringEditing: Bool](./allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [var selectionFollowsFocus: Bool](./selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [class let selectionDidChangeNotification: NSNotification.Name](./selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/allowsmultipleselectionduringediting)*