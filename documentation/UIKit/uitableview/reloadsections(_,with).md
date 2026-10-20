# reloadSections(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads the specified sections using the provided animation effect.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func reloadSections(_ sections: IndexSet, with animation: UITableView.RowAnimation)
```

```objc
- (void) reloadSections:(NSIndexSet *) sections withRowAnimation:(UITableViewRowAnimation) animation;
```

#### Discussion

Calling this method causes the table view to ask its data source for new cells for the specified sections. The table view animates the insertion of new cells in as it animates the old cells out. Call this method if you want to alert the user that the values of the designated sections are changing. If, however, you just want to change values in cells of the specified sections without alerting the user, you can get those cells and directly set their new values.

When this method is called in an animation block defined by the [`beginUpdates()`](./beginupdates%28%29.md) and [`endUpdates()`](./endupdates%28%29.md) methods, it behaves similarly to [`deleteSections(_:with:)`](./deletesections%28_,with%29.md). The indexes that `UITableView` passes to the method are specified in the state of the table view prior to any updates. This happens regardless of ordering of the insertion, deletion, and reloading method calls within the animation block.

## Parameters

- `sections`: An index set identifying the sections to reload.
- `animation`: A constant that indicates how the reloading is to be animated, for example, fade out or slide out from the bottom. See [`UITableView.RowAnimation`](./rowanimation.md) for descriptions of these constants.

  The animation constant affects the direction in which both the old and the new section rows slide. For example, if the animation constant is [`UITableView.RowAnimation.right`](./rowanimation/right.md), the old rows slide out to the right and the new cells slide in from the right.

## See Also

### Related Documentation
- [func insertSections(IndexSet, with: UITableView.RowAnimation)](./insertsections%28_,with%29.md)
  Inserts one or more sections in the table view, with an option to animate the insertion.
### Reloading the table view
- [var hasUncommittedUpdates: Bool](./hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reconfigureRows(at: [IndexPath])](./reconfigurerows%28at%29.md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads the rows and sections of the table view.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](./reloadrows%28at,with%29.md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSectionIndexTitles()](./reloadsectionindextitles%28%29.md)
  Reloads the items in the index bar along the right side of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/reloadsections(_:with:))*