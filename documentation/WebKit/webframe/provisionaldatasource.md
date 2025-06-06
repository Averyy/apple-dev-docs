# provisionalDataSource

**Framework**: Webkit  
**Kind**: property

The provisional data source, or `nil` if either a load request is not in progress or a load request has completed.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var provisionalDataSource: WebDataSource! { get }
```

#### Discussion

Use the [`load(_:)`](webframe/load(_:)-47p2s.md) method to initiate an asynchronous client request, which creates a provisional data source. The provisional data source transitions to a committed data source once any data is received.

## See Also

- [var dataSource: WebDataSource?](webframe/datasource.md)
  The committed data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/provisionaldatasource)*