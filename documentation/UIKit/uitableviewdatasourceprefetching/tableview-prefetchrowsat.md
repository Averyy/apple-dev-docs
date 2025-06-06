# tableView(_:prefetchRowsAt:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Instructs your prefetch data source object to begin preparing data for the cells at the supplied index paths.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func tableView(_ tableView: UITableView, prefetchRowsAt indexPaths: [IndexPath])
```

#### Discussion

The table view calls this method on the main dispatch queue as the user scrolls, providing the index paths for cells it is likely to display in the near future. Use your implementation of this method to start any expensive data loading operations. Always load your data asynchronously and forward the results to your table’s data source object. Table views do not call this method for cells they require immediately, so your data source object must also be able to fetch the data itself.

For information about how to create an asynchronous data loading task, see [`Concurrency Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## Parameters

- `tableView`: The table view issuing the prefetch request.
- `indexPaths`: The index paths that specify the locations of the items for which the data is to be prefetched. The index paths are sorted in ascending order based on their priority. The first index path corresponds to the row closest to the visibile area, and the last index path corresponds to the row furthest from the visible area.

## See Also

- [func tableView(UITableView, cancelPrefetchingForRowsAt: [IndexPath])](uitableviewdatasourceprefetching/tableview(_:cancelprefetchingforrowsat:).md)
  Cancels a previously triggered data prefetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching/tableview(_:prefetchrowsat:))*