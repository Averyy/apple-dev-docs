# defaultRowAnimation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The default type of animation to use when inserting or deleting rows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var defaultRowAnimation: UITableView.RowAnimation { get set }
```

```objc
@property (nonatomic) UITableViewRowAnimation defaultRowAnimation;
```

## Discussion

The default value of this property is [`UITableView.RowAnimation.automatic`](../uitableview/rowanimation/automatic.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [`applySnapshot(_:animatingDifferences:)`](./applysnapshot%28_,animatingdifferences%29.md) or [`applySnapshot(_:animatingDifferences:completion:)`](./applysnapshot%28_,animatingdifferences,completion%29.md).

## See Also

### Updating data
- [func snapshot() -> NSDiffableDataSourceSnapshotReference](./snapshot%28%29.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](./applysnapshot%28_,animatingdifferences%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](./applysnapshot%28_,animatingdifferences,completion%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference)](./applysnapshot%28usingreloaddata%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)?)](./applysnapshot%28usingreloaddata,completion%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/defaultrowanimation)*