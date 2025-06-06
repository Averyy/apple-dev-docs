# nextFocusedIndexPath

**Framework**: UIKit  
**Kind**: property

Returns the index path of the cell containing the context’s next focused view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var nextFocusedIndexPath: IndexPath? { get }
```

#### Discussion

This property returns the index path only when the [`nextFocusedView`](uifocusupdatecontext/nextfocusedview.md) is located within a cell of the table view. Otherwise, it returns `nil`. This can happen if focus is moving out of the table view, because the [`nextFocusedView`](uifocusupdatecontext/nextfocusedview.md) isn’t associated with an index path in this table view.

When focus is moving from one table view to another, each table view delegate is called with [`previouslyFocusedIndexPath`](uitableviewfocusupdatecontext/previouslyfocusedindexpath.md) and [`nextFocusedIndexPath`](uitableviewfocusupdatecontext/nextfocusedindexpath.md) configured for its specific table view.

## See Also

- [var previouslyFocusedIndexPath: IndexPath?](uitableviewfocusupdatecontext/previouslyfocusedindexpath.md)
  Returns the index path of the cell containing the context’s previously focused view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext/nextfocusedindexpath)*