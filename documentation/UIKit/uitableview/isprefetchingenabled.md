# isPrefetchingEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether to allow cell and data prefetching.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isPrefetchingEnabled: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/Swift/true), the table view may request cells in advance of displaying them. When [`false`](https://developer.apple.com/documentation/Swift/false), the table view requests cells when they need to display. Setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) also disables data prefetching. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var dataSource: (any UITableViewDataSource)?](uitableview/datasource.md)
  The object that acts as the data source of the table view.
- [var prefetchDataSource: (any UITableViewDataSourcePrefetching)?](uitableview/prefetchdatasource.md)
  The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.
- [protocol UITableViewDataSource](uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [protocol UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/isprefetchingenabled)*