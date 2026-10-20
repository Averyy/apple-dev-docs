# pageTitle

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The title of the data source’s page.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var pageTitle: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * pageTitle;
```

#### Discussion

The associated web view notifies its frame load delegate when the page title is loaded by invoking the `webView:didReceiveTitle:forFrame:` delegate method.

`nil` if the page has no title or the page title hasn’t been loaded yet.

## See Also

### Querying page data and state
- [var data: Data!](./data.md)
  The raw data that represents the data source’s content.
- [var isLoading: Bool](./isloading.md)
  A Boolean that indicates whether the data source is loading its content.
- [var representation: (any WebDocumentRepresentation)!](./representation.md)
  The data source’s representation depending on its MIME type.
- [var textEncodingName: String!](./textencodingname.md)
  The text encoding for the data source’s web view, if set, or the text encoding of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/pagetitle)*