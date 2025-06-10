# Working With Document Web Views (Legacy)

**Framework**: WebKit

## Topics

### Working With Document Web Views (Legacy)
- [protocol WebDocumentRepresentation](webdocumentrepresentation.md)
  This protocol is adopted by document representation classes that handle specific MIME types. You can implement your own document view classes and document representation classes to render data for specific MIME types, and register those classes using the `WebFrame` [`registerClass(_:representationClass:forMIMEType:)`](webview-swift.class/registerclass(_:representationclass:formimetype:).md) method.
- [protocol WebDocumentSearching](webdocumentsearching.md)
  `WebDocumentSearching` is an optional protocol for document view objects that support searching. Classes that adopt this protocol should also adopt `WebDocumentView` and inherit from `NSView`.
- [protocol WebDocumentText](webdocumenttext.md)
  `WebDocumentText` is an optional protocol for document view objects that display text. This protocol defines methods for accessing document content as strings, and methods for text selection. Classes that adopt this protocol should also adopt [`WebDocumentView`](webdocumentview.md) and inherit from `NSView`.
- [protocol WebDocumentView](webdocumentview.md)
  This protocol is adopted by the document view of a `WebFrameView`. You can extend WebKit to support additional MIME types by implementing your own document view and document representation classes to render data for specific MIME types. You register those classes using the WebFrame [`registerClass(_:representationClass:forMIMEType:)`](webview-swift.class/registerclass(_:representationclass:formimetype:).md) method. Classes that adopt this protocol are expected to be subclasses of `NSView`.

## See Also

- [Document Object Models API (Legacy)](document-object-models-api-legacy.md)
- [Setting Up a Web View (Legacy)](setting-up-a-web-view-legacy.md)
- [Accessing Previous Webpages (Legacy)](accessing-previous-webpages-legacy.md)
- [Archiving Webpages (Legacy)](archiving-webpages-legacy.md)
- [Loading Resources (Legacy)](loading-resources-legacy.md)
- [Working with Frames (legacy)](working-with-frames-legacy.md)
- [Downloading Information (Legacy)](downloading-information-legacy.md)
- [Opening a File (Legacy)](opening-a-file-legacy.md)
- [Setting Policies (Legacy)](setting-policies-legacy.md)
- [Implementing Plugins (Legacy)](implementing-plugins-legacy.md)
- [Incorporating Scripts (Legacy)](incorporating-scripts-legacy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/working-with-document-web-views-legacy)*