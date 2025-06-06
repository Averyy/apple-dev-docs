# data

**Framework**: Webkit  
**Kind**: property

The raw data that represents the data source’s content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var data: Data! { get }
```

#### Discussion

The format of the data is dependent on the data source’s MIME type (obtained from the response).

## See Also

- [var isLoading: Bool](webdatasource/isloading.md)
  A Boolean that indicates whether the data source is loading its content.
- [var pageTitle: String!](webdatasource/pagetitle.md)
  The title of the data source’s page.
- [var representation: (any WebDocumentRepresentation)!](webdatasource/representation.md)
  The data source’s representation depending on its MIME type.
- [var textEncodingName: String!](webdatasource/textencodingname.md)
  The text encoding for the data source’s web view, if set, or the text encoding of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/data)*