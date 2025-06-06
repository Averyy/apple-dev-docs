# canShowMIMEType(_:)

**Framework**: Webkit  
**Kind**: method

Returns whether the receiver can display content of a given MIME type.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func canShowMIMEType(_ MIMEType: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver can display content of the specified MIME type where `MIMEType` is one of the standard types like “image/gif”; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `MIMEType`: The MIME type of the content.

## See Also

- [class func mimeTypesShownAsHTML() -> [Any]!](webview/mimetypesshownashtml.md)
  Returns a list of MIME types that WebKit renders as HTML.
- [class func setMIMETypesShownAsHTML([Any]!)](webview/setmimetypesshownashtml(_:).md)
  Sets the MIME types that WebKit attempts to render as HTML.
- [class func canShowMIMEType(asHTML: String!) -> Bool](webview/canshowmimetype(ashtml:).md)
  Returns whether the receiver interprets a MIME type as HTML.
- [var supportsTextEncoding: Bool](webview/supportstextencoding.md)
  A Boolean that indicates whether the document view supports different text encodings.
- [var customTextEncodingName: String!](webview/customtextencodingname.md)
  The custom text encoding name.
- [var textSizeMultiplier: Float](webview/textsizemultiplier.md)
  The font size multiplier for text displayed in web frame view objects managed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/canshowmimetype(_:))*