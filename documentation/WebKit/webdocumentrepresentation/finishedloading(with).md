# finishedLoading(with:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invoked when a data source finishes loading its content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func finishedLoading(with dataSource: WebDataSource!)
```

```objc
- (void) finishedLoadingWithDataSource:(WebDataSource *) dataSource;
```

## Parameters

- `dataSource`: A `WebDataSource` object that identifies the request that finished loading.

## See Also

### Related Documentation
- [func setDataSource(WebDataSource!)](./setdatasource%28_%29.md)
  Sets the receiver’s data source.
### Loading content
- [func receivedData(Data!, with: WebDataSource!)](./receiveddata%28_,with%29.md)
  Invoked when a data source has received some data.
- [func receivedError((any Error)!, with: WebDataSource!)](./receivederror%28_,with%29.md)
  Invoked when a data source receives an error loading its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/finishedloading(with:))*