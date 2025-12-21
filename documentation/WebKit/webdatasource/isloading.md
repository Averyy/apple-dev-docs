# isLoading

**Framework**: WebKit  
**Kind**: property

A Boolean that indicates whether the data source is loading its content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var isLoading: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the data source is in the process of loading its content; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var data: Data!](webdatasource/data.md)
  The raw data that represents the data source’s content.
- [var pageTitle: String!](webdatasource/pagetitle.md)
  The title of the data source’s page.
- [var representation: (any WebDocumentRepresentation)!](webdatasource/representation.md)
  The data source’s representation depending on its MIME type.
- [var textEncodingName: String!](webdatasource/textencodingname.md)
  The text encoding for the data source’s web view, if set, or the text encoding of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/isloading)*