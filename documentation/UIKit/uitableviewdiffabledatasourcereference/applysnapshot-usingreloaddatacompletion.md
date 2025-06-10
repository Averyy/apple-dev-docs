# applySnapshot(usingReloadData:completion:)

**Framework**: UIKit  
**Kind**: method

Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func applySnapshot(usingReloadData snapshot: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)? = nil)
```

#### Discussion

The system interrupts any ongoing item animations and immediately reloads the table view’s content.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the table view.
- `completion`: A closure to execute when the reload completes. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshotReference](uitableviewdiffabledatasourcereference/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](uitableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference)](uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [var defaultRowAnimation: UITableView.RowAnimation](uitableviewdiffabledatasourcereference/defaultrowanimation.md)
  The default type of animation to use when inserting or deleting rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:completion:))*