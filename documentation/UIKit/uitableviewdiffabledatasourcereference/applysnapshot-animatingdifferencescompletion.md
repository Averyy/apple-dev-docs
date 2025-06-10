# applySnapshot(_:animatingDifferences:completion:)

**Framework**: UIKit  
**Kind**: method

Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func applySnapshot(_ snapshot: NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)? = nil)
```

#### Discussion

The diffable data source computes the difference between the table view’s current state and the new state in the applied snapshot, which is an O() operation, where  is the number of items in the snapshot.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the table view.
- `animatingDifferences`: If  , the system animates the updates to the table view. If  , the system doesn’t animate the updates to the table view.
- `completion`: A closure to execute when the animations are complete. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshotReference](uitableviewdiffabledatasourcereference/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference)](uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)?)](uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:completion:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
- [var defaultRowAnimation: UITableView.RowAnimation](uitableviewdiffabledatasourcereference/defaultrowanimation.md)
  The default type of animation to use when inserting or deleting rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:))*