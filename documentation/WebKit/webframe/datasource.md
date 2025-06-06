# dataSource

**Framework**: Webkit  
**Kind**: property

The committed data source.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var dataSource: WebDataSource? { get }
```

#### Discussion

`nil` if the provisional data source is not done loading.

## See Also

- [var provisionalDataSource: WebDataSource!](webframe/provisionaldatasource.md)
  The provisional data source, or `nil` if either a load request is not in progress or a load request has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframe/datasource)*