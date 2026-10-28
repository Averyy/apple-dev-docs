# dataSource

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that acts as the data source of the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
weak var dataSource: (any UITableViewDataSource)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UITableViewDataSource> dataSource;
```

## Discussion

The data source must adopt the [`UITableViewDataSource`](../uitableviewdatasource.md) protocol. The data source isn’t retained.

## See Also

### Related Documentation
- [var delegate: (any UITableViewDelegate)?](./delegate.md)
  The object that acts as the delegate of the table view.
### Providing the data and cells
- [var prefetchDataSource: (any UITableViewDataSourcePrefetching)?](./prefetchdatasource.md)
  The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.
- [var isPrefetchingEnabled: Bool](./isprefetchingenabled.md)
  A Boolean value that indicates whether to allow cell and data prefetching.
- [protocol UITableViewDataSource](../uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [protocol UITableViewDataSourcePrefetching](../uitableviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/datasource)*