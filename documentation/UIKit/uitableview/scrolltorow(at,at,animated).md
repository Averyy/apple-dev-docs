# scrollToRow(at:at:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Scrolls through the table view until a row that an index path identifies is at a particular location on the screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func scrollToRow(at indexPath: IndexPath, at scrollPosition: UITableView.ScrollPosition, animated: Bool)
```

```objc
- (void) scrollToRowAtIndexPath:(NSIndexPath *) indexPath atScrollPosition:(UITableViewScrollPosition) scrollPosition animated:(BOOL) animated;
```

#### Discussion

Invoking this method doesn’t cause the delegate to receive a [`scrollViewDidScroll(_:)`](../uiscrollviewdelegate/scrollviewdidscroll%28_%29.md) message, as is normal for programmatically invoked user interface operations.

## Parameters

- `indexPath`: An index path that identifies a row in the table view by its row index and its section index.

  `NSNotFound` is a valid row index for scrolling to a section with zero rows.
- `scrollPosition`: A constant that identifies a relative position in the table view (top, middle, bottom) for `row` when scrolling concludes. See [`UITableView.ScrollPosition`](./scrollposition.md) for descriptions of valid constants.
- `animated`: [`true`](../../Swift/true.md) if you want to animate the change in position; [`false`](../../Swift/false.md) if it should be immediate.

## See Also

### Scrolling the table view
- [func scrollToNearestSelectedRow(at: UITableView.ScrollPosition, animated: Bool)](./scrolltonearestselectedrow%28at,animated%29.md)
  Scrolls the table view so that the selected row nearest to a specified position in the table view is at that position.
- [UITableView.ScrollPosition](./scrollposition.md)
  The position in the table view (top, middle, bottom) to scroll a specified row to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/scrolltorow(at:at:animated:))*