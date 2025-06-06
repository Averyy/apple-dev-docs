# drop(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Animates the item to the specified location and inserts a placeholder cell at that location.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func drop(_ dragItem: UIDragItem, to placeholder: UITableViewDropPlaceholder) -> any UITableViewDropPlaceholderContext
```

#### Return Value

The context object that you use to replace or remove the placeholder cell later. Store a reference to this object so that you can call its methods later.

#### Discussion

Use this method to insert a temporary placeholder cell (instead of a cell backed by actual data) into the table view. When calling this method, do not update your data source object to account for the placeholder. The table view manages the placeholder until you explicitly remove it using the returned context object.

Typically, you use this method when you must load data asynchronously for a cell. Instead of updating your data source, you insert a placeholder cell. When the data is finally available, update your data source object and call the [`commitInsertion(dataSourceUpdates:)`](uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates:).md) method of the returned context object to swap out the placeholder cell for an actual cell. You can also remove a placeholder cell that is no longer needed by calling the [`deletePlaceholder()`](uitableviewdropplaceholdercontext/deleteplaceholder().md) method.

At some point after calling this method, the table view executes the [`cellUpdateHandler`](uitableviewplaceholder/cellupdatehandler.md) block in the provided `placeholder` object. Use that block to configure the contents of the placeholder cell.

## Parameters

- `dragItem`: The drag item containing the data to drop.
- `placeholder`: The object that contains information about the type of placeholder cell to insert, and where to insert it.

## See Also

- [func drop(UIDragItem, toRowAt: IndexPath) -> any UIDragAnimating](uitableviewdropcoordinator/drop(_:torowat:).md)
  Animates the item to the specified index path in the table view.
- [func drop(UIDragItem, intoRowAt: IndexPath, rect: CGRect) -> any UIDragAnimating](uitableviewdropcoordinator/drop(_:intorowat:rect:).md)
- [func drop(UIDragItem, to: UIDragPreviewTarget) -> any UIDragAnimating](uitableviewdropcoordinator/drop(_:to:)-57wx.md)
  Animates the item to an arbitrary location in your view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropcoordinator/drop(_:to:)-3znax)*