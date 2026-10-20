# isLoading

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the data source is loading its content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var isLoading: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLoading) BOOL loading;
```

#### Discussion

[`true`](../../Swift/true.md) if the data source is in the process of loading its content; otherwise, [`false`](../../Swift/false.md).

## See Also

### Querying page data and state
- [var data: Data!](./data.md)
  The raw data that represents the data source’s content.
- [var pageTitle: String!](./pagetitle.md)
  The title of the data source’s page.
- [var representation: (any WebDocumentRepresentation)!](./representation.md)
  The data source’s representation depending on its MIME type.
- [var textEncodingName: String!](./textencodingname.md)
  The text encoding for the data source’s web view, if set, or the text encoding of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdatasource/isloading)*