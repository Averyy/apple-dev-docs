# receivedData(_:with:)

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Invoked when a data source has received some data.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func receivedData(_ data: Data!, with dataSource: WebDataSource!)
```

#### Discussion

Data is loaded incrementally, so this method may be invoked multiple times. The receiver is responsible for accumulating this data.

## Parameters

- `data`: An   object containing the data received.
- `dataSource`: A   object that identifies the request that generated this data.

## See Also

- [func receivedError((any Error)!, with: WebDataSource!)](webdocumentrepresentation/receivederror(_:with:).md)
  Invoked when a data source receives an error loading its content.
- [func finishedLoading(with: WebDataSource!)](webdocumentrepresentation/finishedloading(with:).md)
  Invoked when a data source finishes loading its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/receiveddata(_:with:))*