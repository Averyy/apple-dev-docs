# receivedError(_:with:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Invoked when a data source receives an error loading its content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func receivedError(_ error: (any Error)!, with dataSource: WebDataSource!)
```

#### Discussion

The `error` argument contains details on the error that occurred.

## Parameters

- `error`: An   object that indicates what error occurred.
- `dataSource`: A   object that identifies the request that caused this error.

## See Also

- [func receivedData(Data!, with: WebDataSource!)](webdocumentrepresentation/receiveddata(_:with:).md)
  Invoked when a data source has received some data.
- [func finishedLoading(with: WebDataSource!)](webdocumentrepresentation/finishedloading(with:).md)
  Invoked when a data source finishes loading its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation/receivederror(_:with:))*