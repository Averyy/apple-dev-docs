# isPrefetchingEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow cell and data prefetching.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var isPrefetchingEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isPrefetchingEnabled) BOOL prefetchingEnabled;
```

## Discussion

When [`true`](../../Swift/true.md), the table view may request cells in advance of displaying them. When [`false`](../../Swift/false.md), the table view requests cells when they need to display. Setting this property to [`false`](../../Swift/false.md) also disables data prefetching. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Providing the data and cells
- [var dataSource: (any UITableViewDataSource)?](./datasource.md)
  The object that acts as the data source of the table view.
- [var prefetchDataSource: (any UITableViewDataSourcePrefetching)?](./prefetchdatasource.md)
  The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.
- [protocol UITableViewDataSource](../uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [protocol UITableViewDataSourcePrefetching](../uitableviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/isprefetchingenabled)*