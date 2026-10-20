# receivedData(_:with:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invoked when a data source has received some data.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func receivedData(_ data: Data!, with dataSource: WebDataSource!)
```

```objc
- (void) receivedData:(NSData *) data withDataSource:(WebDataSource *) dataSource;
```

#### Discussion

Data is loaded incrementally, so this method may be invoked multiple times. The receiver is responsible for accumulating this data.

## Parameters

- `data`: An `NSData` object containing the data received.
- `dataSource`: A `WebDataSource` object that identifies the request that generated this data.

## See Also

### Loading content
- [func receivedError((any Error)!, with: WebDataSource!)](./receivederror%28_,with%29.md)
  Invoked when a data source receives an error loading its content.
- [func finishedLoading(with: WebDataSource!)](./finishedloading%28with%29.md)
  Invoked when a data source finishes loading its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/receiveddata(_:with:))*