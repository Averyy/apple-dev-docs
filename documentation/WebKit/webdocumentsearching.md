# WebDocumentSearching

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

`WebDocumentSearching` is an optional protocol for document view objects that support searching. Classes that adopt this protocol should also adopt `WebDocumentView` and inherit from `NSView`.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebDocumentSearching : NSObjectProtocol
```

```objc
@protocol WebDocumentSearching <NSObject>
```

## Topics

### Searching a document
- [func search(for: String!, direction: Bool, caseSensitive: Bool, wrap: Bool) -> Bool](./webdocumentsearching/search%28for,direction,casesensitive,wrap%29.md)
  Searches for a string in a given direction from the current position.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working With Document Web Views (Legacy)
- [protocol WebDocumentRepresentation](./webdocumentrepresentation.md)
  This protocol is adopted by document representation classes that handle specific MIME types. You can implement your own document view classes and document representation classes to render data for specific MIME types, and register those classes using the `WebFrame` [`registerClass(_:representationClass:forMIMEType:)`](./webview-swift.class/registerclass%28_,representationclass,formimetype%29.md) method.
- [protocol WebDocumentText](./webdocumenttext.md)
  `WebDocumentText` is an optional protocol for document view objects that display text. This protocol defines methods for accessing document content as strings, and methods for text selection. Classes that adopt this protocol should also adopt [`WebDocumentView`](./webdocumentview.md) and inherit from `NSView`.
- [protocol WebDocumentView](./webdocumentview.md)
  This protocol is adopted by the document view of a `WebFrameView`. You can extend WebKit to support additional MIME types by implementing your own document view and document representation classes to render data for specific MIME types. You register those classes using the WebFrame [`registerClass(_:representationClass:forMIMEType:)`](./webview-swift.class/registerclass%28_,representationclass,formimetype%29.md) method. Classes that adopt this protocol are expected to be subclasses of `NSView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentsearching)*