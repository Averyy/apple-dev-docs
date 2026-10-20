# WebDocumentRepresentation

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

This protocol is adopted by document representation classes that handle specific MIME types. You can implement your own document view classes and document representation classes to render data for specific MIME types, and register those classes using the `WebFrame` [`registerClass(_:representationClass:forMIMEType:)`](./webview-swift.class/registerclass%28_,representationclass,formimetype%29.md) method.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebDocumentRepresentation : NSObjectProtocol
```

```objc
@protocol WebDocumentRepresentation <NSObject>
```

## Topics

### Setting the data source
- [func setDataSource(WebDataSource!)](./webdocumentrepresentation/setdatasource%28_%29.md)
  Sets the receiver’s data source.
### Loading content
- [func receivedData(Data!, with: WebDataSource!)](./webdocumentrepresentation/receiveddata%28_,with%29.md)
  Invoked when a data source has received some data.
- [func receivedError((any Error)!, with: WebDataSource!)](./webdocumentrepresentation/receivederror%28_,with%29.md)
  Invoked when a data source receives an error loading its content.
- [func finishedLoading(with: WebDataSource!)](./webdocumentrepresentation/finishedloading%28with%29.md)
  Invoked when a data source finishes loading its content.
### Getting document source
- [func canProvideDocumentSource() -> Bool](./webdocumentrepresentation/canprovidedocumentsource%28%29.md)
  Returns whether the receiver can provide content source.
- [func documentSource() -> String!](./webdocumentrepresentation/documentsource%28%29.md)
  Returns the receiver’s source as text.
### Getting the document title
- [func title() -> String!](./webdocumentrepresentation/title%28%29.md)
  Returns the receiver’s document title.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working With Document Web Views (Legacy)
- [protocol WebDocumentSearching](./webdocumentsearching.md)
  `WebDocumentSearching` is an optional protocol for document view objects that support searching. Classes that adopt this protocol should also adopt `WebDocumentView` and inherit from `NSView`.
- [protocol WebDocumentText](./webdocumenttext.md)
  `WebDocumentText` is an optional protocol for document view objects that display text. This protocol defines methods for accessing document content as strings, and methods for text selection. Classes that adopt this protocol should also adopt [`WebDocumentView`](./webdocumentview.md) and inherit from `NSView`.
- [protocol WebDocumentView](./webdocumentview.md)
  This protocol is adopted by the document view of a `WebFrameView`. You can extend WebKit to support additional MIME types by implementing your own document view and document representation classes to render data for specific MIME types. You register those classes using the WebFrame [`registerClass(_:representationClass:forMIMEType:)`](./webview-swift.class/registerclass%28_,representationclass,formimetype%29.md) method. Classes that adopt this protocol are expected to be subclasses of `NSView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentrepresentation)*