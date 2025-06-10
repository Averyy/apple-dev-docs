# defaultRowAnimation

**Framework**: UIKit  
**Kind**: property

The default type of animation to use when inserting or deleting rows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var defaultRowAnimation: UITableView.RowAnimation { get set }
```

#### Discussion

The default value of this property is [`UITableView.RowAnimation.automatic`](uitableview/rowanimation/automatic.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [`applySnapshot(_:animatingDifferences:)`](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md) or [`applySnapshot(_:animatingDifferences:completion:)`](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:).md).

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshotReference](uitableviewdiffabledatasourcereference/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference)](uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)?)](uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:completion:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/defaultrowanimation)*