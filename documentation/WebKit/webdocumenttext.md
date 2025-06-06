# WebDocumentText

**Framework**: Webkit  
**Kind**: protocol

`WebDocumentText` is an optional protocol for document view objects that display text. This protocol defines methods for accessing document content as strings, and methods for text selection. Classes that adopt this protocol should also adopt [`WebDocumentView`](webdocumentview.md) and inherit from `NSView`.

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol WebDocumentText : NSObjectProtocol
```

## Topics

### Getting document content
- [func string() -> String!](webdocumenttext/string.md)
  Returns the entire content of the web document as a string.
- [func attributedString() -> NSAttributedString!](webdocumenttext/attributedstring.md)
  Returns the entire content of the web document as an attributed string.
### Selecting and deselecting text
- [func selectAll()](webdocumenttext/selectall.md)
  Selects all the text in the web document.
- [func deselectAll()](webdocumenttext/deselectall.md)
  Deselects the currently selected text in the web document.
- [func selectedString() -> String!](webdocumenttext/selectedstring.md)
  Returns the currently selected text in the web document as a string.
- [func selectedAttributedString() -> NSAttributedString!](webdocumenttext/selectedattributedstring.md)
  Returns the currently selected text in the web document as an attributed string.
### Text encoding
- [func supportsTextEncoding() -> Bool](webdocumenttext/supportstextencoding.md)
  Returns a Boolean value that indicates whether the web document supports text encoding.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol WebDocumentRepresentation](webdocumentrepresentation.md)
  This protocol is adopted by document representation classes that handle specific MIME types. You can implement your own document view classes and document representation classes to render data for specific MIME types, and register those classes using the `WebFrame` [`registerClass(_:representationClass:forMIMEType:)`](webview/registerclass(_:representationclass:formimetype:).md) method.
- [protocol WebDocumentSearching](webdocumentsearching.md)
  `WebDocumentSearching` is an optional protocol for document view objects that support searching. Classes that adopt this protocol should also adopt `WebDocumentView` and inherit from `NSView`.
- [protocol WebDocumentView](webdocumentview.md)
  This protocol is adopted by the document view of a `WebFrameView`. You can extend WebKit to support additional MIME types by implementing your own document view and document representation classes to render data for specific MIME types. You register those classes using the WebFrame [`registerClass(_:representationClass:forMIMEType:)`](webview/registerclass(_:representationclass:formimetype:).md) method. Classes that adopt this protocol are expected to be subclasses of `NSView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumenttext)*