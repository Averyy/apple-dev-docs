# tableView(_:cancelPrefetchingForRowsAt:)

**Framework**: UIKit  
**Kind**: method

Cancels a previously triggered data prefetch request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, cancelPrefetchingForRowsAt indexPaths: [IndexPath])
```

#### Discussion

The table view calls this method on the main queue to cancel prefetch requests for cells that are no longer needed. Use this method to cancel operations initiated by a previous call to [`tableView(_:prefetchRowsAt:)`](uitableviewdatasourceprefetching/tableview(_:prefetchrowsat:).md).

For information about how to cancel an asynchronous data loading task, see [`Concurrency Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## Parameters

- `tableView`: The table view issuing the cancellation of the prefetch request.
- `indexPaths`: The index paths of the items for which the data is no longer required.

## See Also

- [func tableView(UITableView, prefetchRowsAt: [IndexPath])](uitableviewdatasourceprefetching/tableview(_:prefetchrowsat:).md)
  Instructs your prefetch data source object to begin preparing data for the cells at the supplied index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching/tableview(_:cancelprefetchingforrowsat:))*