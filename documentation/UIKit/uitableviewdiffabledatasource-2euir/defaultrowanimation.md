# defaultRowAnimation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The default type of animation to use when inserting or deleting rows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var defaultRowAnimation: UITableView.RowAnimation { get set }
```

#### Discussion

The default value of this property is [`UITableView.RowAnimation.automatic`](../uitableview/rowanimation/automatic.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [`apply(_:animatingDifferences:completion:)`](./apply%28_,animatingdifferences,completion%29.md).

## See Also

### Updating data
- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](./snapshot%28%29.md)
  Returns a representation of the current state of the data in the table view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool) async](./apply%28_,animatingdifferences%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](./apply%28_,animatingdifferences,completion%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>) async](./applysnapshotusingreloaddata%28_%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, completion: (() -> Void)?)](./applysnapshotusingreloaddata%28_,completion%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/defaultrowanimation)*