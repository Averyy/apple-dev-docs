# dataSource

**Framework**: UIKit  
**Kind**: property

The object that acts as the data source of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var dataSource: (any UITableViewDataSource)? { get set }
```

#### Discussion

The data source must adopt the [`UITableViewDataSource`](uitableviewdatasource.md) protocol. The data source isn’t retained.

## See Also

- [var delegate: (any UITableViewDelegate)?](uitableview/delegate.md)
  The object that acts as the delegate of the table view.
- [var prefetchDataSource: (any UITableViewDataSourcePrefetching)?](uitableview/prefetchdatasource.md)
  The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.
- [var isPrefetchingEnabled: Bool](uitableview/isprefetchingenabled.md)
  A Boolean value that indicates whether to allow cell and data prefetching.
- [protocol UITableViewDataSource](uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [protocol UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/datasource)*