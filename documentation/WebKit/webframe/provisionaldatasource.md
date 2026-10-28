# provisionalDataSource

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The provisional data source, or `nil` if either a load request is not in progress or a load request has completed.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var provisionalDataSource: WebDataSource! { get }
```

```objc
@property (nonatomic, strong, readonly) WebDataSource * provisionalDataSource;
```

## Discussion

Use the [`load(_:)`](./load%28_%29-47p2s.md) method to initiate an asynchronous client request, which creates a provisional data source. The provisional data source transitions to a committed data source once any data is received.

## See Also

### Getting the Data Source
- [var dataSource: WebDataSource?](./datasource.md)
  The committed data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/provisionaldatasource)*