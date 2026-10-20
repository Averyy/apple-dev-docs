# dataSource

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The committed data source.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var dataSource: WebDataSource? { get }
```

```objc
@property (nonatomic, strong, readonly) WebDataSource * dataSource;
```

#### Discussion

`nil` if the provisional data source is not done loading.

## See Also

### Getting the Data Source
- [var provisionalDataSource: WebDataSource!](./provisionaldatasource.md)
  The provisional data source, or `nil` if either a load request is not in progress or a load request has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/datasource)*