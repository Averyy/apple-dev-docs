# representation

**Framework**: WebKit  
**Kind**: property

The data source’s representation depending on its MIME type.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var representation: (any WebDocumentRepresentation)! { get }
```

#### Discussion

`nil` if the data source is in the process of being loaded and this method is invoked before loading is complete.

You can specify the mapping between a representation and MIME type using the ``WebView/registerClass(_:representationClass:forMIMEType:)```WebView` class method.

## See Also

- [var data: Data!](webdatasource/data.md)
  The raw data that represents the data source’s content.
- [var isLoading: Bool](webdatasource/isloading.md)
  A Boolean that indicates whether the data source is loading its content.
- [var pageTitle: String!](webdatasource/pagetitle.md)
  The title of the data source’s page.
- [var textEncodingName: String!](webdatasource/textencodingname.md)
  The text encoding for the data source’s web view, if set, or the text encoding of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/representation)*