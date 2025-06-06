# defaultRowAnimation

**Framework**: UIKit  
**Kind**: property

The default type of animation to use when inserting or deleting rows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var defaultRowAnimation: UITableView.RowAnimation { get set }
```

#### Discussion

The default value of this property is [`UITableView.RowAnimation.automatic`](uitableview/rowanimation/automatic.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [`apply(_:animatingDifferences:completion:)`](uitableviewdiffabledatasource-2euir/apply(_:animatingdifferences:completion:).md).

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](uitableviewdiffabledatasource-2euir/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool) async](uitableviewdiffabledatasource-2euir/apply(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](uitableviewdiffabledatasource-2euir/apply(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>) async](uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata(_:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, completion: (() -> Void)?)](uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata(_:completion:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/defaultrowanimation)*