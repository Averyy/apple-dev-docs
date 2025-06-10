# finishedLoading(with:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Invoked when a data source finishes loading its content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func finishedLoading(with dataSource: WebDataSource!)
```

## Parameters

- `dataSource`: A   object that identifies the request that finished loading.

## See Also

- [func setDataSource(WebDataSource!)](webdocumentrepresentation/setdatasource(_:).md)
  Sets the receiver’s data source.
- [func receivedData(Data!, with: WebDataSource!)](webdocumentrepresentation/receiveddata(_:with:).md)
  Invoked when a data source has received some data.
- [func receivedError((any Error)!, with: WebDataSource!)](webdocumentrepresentation/receivederror(_:with:).md)
  Invoked when a data source receives an error loading its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/finishedloading(with:))*