# textEncodingName

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The text encoding for the data source’s web view, if set, or the text encoding of the response.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var textEncodingName: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * textEncodingName;
```

## See Also

### Querying page data and state
- [var data: Data!](./data.md)
  The raw data that represents the data source’s content.
- [var isLoading: Bool](./isloading.md)
  A Boolean that indicates whether the data source is loading its content.
- [var pageTitle: String!](./pagetitle.md)
  The title of the data source’s page.
- [var representation: (any WebDocumentRepresentation)!](./representation.md)
  The data source’s representation depending on its MIME type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/textencodingname)*