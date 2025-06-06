# drop(_:toRowAt:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Animates the item to the specified index path in the table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func drop(_ dragItem: UIDragItem, toRowAt indexPath: IndexPath) -> any UIDragAnimating
```

## Mentions

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

#### Discussion

Use this method to animate the dragged item to the specific location in the table view. Typically, you use this method for content that originated in the collection view and is moving to a new location.

## Parameters

- `dragItem`: The dragged item that you want to animate into position.
- `indexPath`: The index path to use as the destination for the animation.

## See Also

- [func drop(UIDragItem, intoRowAt: IndexPath, rect: CGRect) -> any UIDragAnimating](uitableviewdropcoordinator/drop(_:intorowat:rect:).md)
- [func drop(UIDragItem, to: UIDragPreviewTarget) -> any UIDragAnimating](uitableviewdropcoordinator/drop(_:to:)-57wx.md)
  Animates the item to an arbitrary location in your view hierarchy.
- [func drop(UIDragItem, to: UITableViewDropPlaceholder) -> any UITableViewDropPlaceholderContext](uitableviewdropcoordinator/drop(_:to:)-3znax.md)
  Animates the item to the specified location and inserts a placeholder cell at that location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdropcoordinator/drop(_:torowat:))*