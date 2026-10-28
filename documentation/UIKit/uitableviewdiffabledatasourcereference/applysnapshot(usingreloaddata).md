# applySnapshot(usingReloadData:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func applySnapshot(usingReloadData snapshot: NSDiffableDataSourceSnapshotReference)
```

```objc
- (void) applySnapshotUsingReloadData:(NSDiffableDataSourceSnapshot<id,id> *) snapshot;
```

## Discussion

The system interrupts any ongoing item animations and immediately reloads the table view’s content.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the table view.

## See Also

### Updating data
- [func snapshot() -> NSDiffableDataSourceSnapshotReference](./snapshot%28%29.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](./applysnapshot%28_,animatingdifferences%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](./applysnapshot%28_,animatingdifferences,completion%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)?)](./applysnapshot%28usingreloaddata,completion%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
- [var defaultRowAnimation: UITableView.RowAnimation](./defaultrowanimation.md)
  The default type of animation to use when inserting or deleting rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:))*