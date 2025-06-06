# prefetchDataSource

**Framework**: UIKit  
**Kind**: property

The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var prefetchDataSource: (any UITableViewDataSourcePrefetching)? { get set }
```

#### Discussion

Assign an object that conforms to the [`UITableViewDataSourcePrefetching`](uitableviewdatasourceprefetching.md) protocol to facilitate prefetching of data for cells to be displayed in the near future. To disable prefetching behavior, set this property to `nil`. This object isn’t retained.

## See Also

- [var dataSource: (any UITableViewDataSource)?](uitableview/datasource.md)
  The object that acts as the data source of the table view.
- [var isPrefetchingEnabled: Bool](uitableview/isprefetchingenabled.md)
  A Boolean value that indicates whether to allow cell and data prefetching.
- [protocol UITableViewDataSource](uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [protocol UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/prefetchdatasource)*