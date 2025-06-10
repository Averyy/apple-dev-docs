# snapshot()

**Framework**: UIKit  
**Kind**: method

Returns a representation of the current state of the data in the table view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func snapshot() -> NSDiffableDataSourceSnapshotReference
```

## See Also

- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference)](uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)?)](uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:completion:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
- [var defaultRowAnimation: UITableView.RowAnimation](uitableviewdiffabledatasourcereference/defaultrowanimation.md)
  The default type of animation to use when inserting or deleting rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/snapshot())*