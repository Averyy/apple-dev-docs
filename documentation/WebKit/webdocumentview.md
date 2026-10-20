# WebDocumentView

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

This protocol is adopted by the document view of a `WebFrameView`. You can extend WebKit to support additional MIME types by implementing your own document view and document representation classes to render data for specific MIME types. You register those classes using the WebFrame [`registerClass(_:representationClass:forMIMEType:)`](./webview-swift.class/registerclass%28_,representationclass,formimetype%29.md) method. Classes that adopt this protocol are expected to be subclasses of `NSView`.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebDocumentView : NSObjectProtocol
```

```objc
@protocol WebDocumentView <NSObject>
```

## Topics

### Setting the data source
- [func setDataSource(WebDataSource!)](./webdocumentview/setdatasource%28_%29.md)
  Invoked when the data source for this document has been changed.
- [func dataSourceUpdated(WebDataSource!)](./webdocumentview/datasourceupdated%28_%29.md)
  Invoked when additional data has been received.
### Controlling the layout
- [func setNeedsLayout(Bool)](./webdocumentview/setneedslayout%28_%29.md)
  Sets whether or not the receiver should change its layout.
- [func layout()](./webdocumentview/layout%28%29.md)
  Invoked when the receiver should change its layout immediately.
### Attaching to a window
- [func viewDidMoveToHostWindow()](./webdocumentview/viewdidmovetohostwindow%28%29.md)
  Invoked when a web view’s host window is set.
- [func viewWillMove(toHostWindow: NSWindow!)](./webdocumentview/viewwillmove%28tohostwindow%29.md)
  Invoked when a web view’s host window is about to change.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working With Document Web Views (Legacy)
- [protocol WebDocumentRepresentation](./webdocumentrepresentation.md)
  This protocol is adopted by document representation classes that handle specific MIME types. You can implement your own document view classes and document representation classes to render data for specific MIME types, and register those classes using the `WebFrame` [`registerClass(_:representationClass:forMIMEType:)`](./webview-swift.class/registerclass%28_,representationclass,formimetype%29.md) method.
- [protocol WebDocumentSearching](./webdocumentsearching.md)
  `WebDocumentSearching` is an optional protocol for document view objects that support searching. Classes that adopt this protocol should also adopt `WebDocumentView` and inherit from `NSView`.
- [protocol WebDocumentText](./webdocumenttext.md)
  `WebDocumentText` is an optional protocol for document view objects that display text. This protocol defines methods for accessing document content as strings, and methods for text selection. Classes that adopt this protocol should also adopt [`WebDocumentView`](./webdocumentview.md) and inherit from `NSView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentview)*