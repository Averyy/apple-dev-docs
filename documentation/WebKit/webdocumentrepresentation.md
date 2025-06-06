# WebDocumentRepresentation

**Framework**: Webkit  
**Kind**: protocol

This protocol is adopted by document representation classes that handle specific MIME types. You can implement your own document view classes and document representation classes to render data for specific MIME types, and register those classes using the `WebFrame` [`registerClass(_:representationClass:forMIMEType:)`](webview/registerclass(_:representationclass:formimetype:).md) method.

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol WebDocumentRepresentation : NSObjectProtocol
```

## Topics

### Setting the data source
- [func setDataSource(WebDataSource!)](webdocumentrepresentation/setdatasource(_:).md)
  Sets the receiver’s data source.
### Loading content
- [func receivedData(Data!, with: WebDataSource!)](webdocumentrepresentation/receiveddata(_:with:).md)
  Invoked when a data source has received some data.
- [func receivedError((any Error)!, with: WebDataSource!)](webdocumentrepresentation/receivederror(_:with:).md)
  Invoked when a data source receives an error loading its content.
- [func finishedLoading(with: WebDataSource!)](webdocumentrepresentation/finishedloading(with:).md)
  Invoked when a data source finishes loading its content.
### Getting document source
- [func canProvideDocumentSource() -> Bool](webdocumentrepresentation/canprovidedocumentsource.md)
  Returns whether the receiver can provide content source.
- [func documentSource() -> String!](webdocumentrepresentation/documentsource.md)
  Returns the receiver’s source as text.
### Getting the document title
- [func title() -> String!](webdocumentrepresentation/title.md)
  Returns the receiver’s document title.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol WebDocumentSearching](webdocumentsearching.md)
  `WebDocumentSearching` is an optional protocol for document view objects that support searching. Classes that adopt this protocol should also adopt `WebDocumentView` and inherit from `NSView`.
- [protocol WebDocumentText](webdocumenttext.md)
  `WebDocumentText` is an optional protocol for document view objects that display text. This protocol defines methods for accessing document content as strings, and methods for text selection. Classes that adopt this protocol should also adopt [`WebDocumentView`](webdocumentview.md) and inherit from `NSView`.
- [protocol WebDocumentView](webdocumentview.md)
  This protocol is adopted by the document view of a `WebFrameView`. You can extend WebKit to support additional MIME types by implementing your own document view and document representation classes to render data for specific MIME types. You register those classes using the WebFrame [`registerClass(_:representationClass:forMIMEType:)`](webview/registerclass(_:representationclass:formimetype:).md) method. Classes that adopt this protocol are expected to be subclasses of `NSView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation)*