# receivedError(_:with:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invoked when a data source receives an error loading its content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func receivedError(_ error: (any Error)!, with dataSource: WebDataSource!)
```

```objc
- (void) receivedError:(NSError *) error withDataSource:(WebDataSource *) dataSource;
```

## Discussion

The `error` argument contains details on the error that occurred.

## Parameters

- `error`: An `NSError` object that indicates what error occurred.
- `dataSource`: A `WebDataSource` object that identifies the request that caused this error.

## See Also

### Loading content
- [func receivedData(Data!, with: WebDataSource!)](./receiveddata%28_,with%29.md)
  Invoked when a data source has received some data.
- [func finishedLoading(with: WebDataSource!)](./finishedloading%28with%29.md)
  Invoked when a data source finishes loading its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/receivederror(_:with:))*