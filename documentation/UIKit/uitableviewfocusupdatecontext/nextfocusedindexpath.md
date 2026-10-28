# nextFocusedIndexPath

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the index path of the cell containing the context’s next focused view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var nextFocusedIndexPath: IndexPath? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSIndexPath * nextFocusedIndexPath;
```

## Discussion

This property returns the index path only when the [`nextFocusedView`](../uifocusupdatecontext/nextfocusedview.md) is located within a cell of the table view. Otherwise, it returns `nil`. This can happen if focus is moving out of the table view, because the [`nextFocusedView`](../uifocusupdatecontext/nextfocusedview.md) isn’t associated with an index path in this table view.

When focus is moving from one table view to another, each table view delegate is called with [`previouslyFocusedIndexPath`](./previouslyfocusedindexpath.md) and [`nextFocusedIndexPath`](./nextfocusedindexpath.md) configured for its specific table view.

## See Also

### Locating focusable items in a table view
- [var previouslyFocusedIndexPath: IndexPath?](./previouslyfocusedindexpath.md)
  Returns the index path of the cell containing the context’s previously focused view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewfocusupdatecontext/nextfocusedindexpath)*