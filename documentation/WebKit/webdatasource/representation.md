# representation

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The data source’s representation depending on its MIME type.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var representation: (any WebDocumentRepresentation)! { get }
```

```objc
@property (nonatomic, strong, readonly) id<WebDocumentRepresentation> representation;
```

#### Discussion

`nil` if the data source is in the process of being loaded and this method is invoked before loading is complete.

You can specify the mapping between a representation and MIME type using the ``WebView/registerClass(_:representationClass:forMIMEType:)```WebView` class method.

## See Also

### Querying page data and state
- [var data: Data!](./data.md)
  The raw data that represents the data source’s content.
- [var isLoading: Bool](./isloading.md)
  A Boolean that indicates whether the data source is loading its content.
- [var pageTitle: String!](./pagetitle.md)
  The title of the data source’s page.
- [var textEncodingName: String!](./textencodingname.md)
  The text encoding for the data source’s web view, if set, or the text encoding of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/representation)*