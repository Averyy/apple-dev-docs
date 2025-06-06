# supportsTextEncoding

**Framework**: Webkit  
**Kind**: property

A Boolean that indicates whether the document view supports different text encodings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var supportsTextEncoding: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver’s document view can support different text encodings; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [class func canShowMIMEType(String!) -> Bool](webview/canshowmimetype(_:).md)
  Returns whether the receiver can display content of a given MIME type.
- [class func mimeTypesShownAsHTML() -> [Any]!](webview/mimetypesshownashtml.md)
  Returns a list of MIME types that WebKit renders as HTML.
- [class func setMIMETypesShownAsHTML([Any]!)](webview/setmimetypesshownashtml(_:).md)
  Sets the MIME types that WebKit attempts to render as HTML.
- [class func canShowMIMEType(asHTML: String!) -> Bool](webview/canshowmimetype(ashtml:).md)
  Returns whether the receiver interprets a MIME type as HTML.
- [var customTextEncodingName: String!](webview/customtextencodingname.md)
  The custom text encoding name.
- [var textSizeMultiplier: Float](webview/textsizemultiplier.md)
  The font size multiplier for text displayed in web frame view objects managed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/supportstextencoding)*