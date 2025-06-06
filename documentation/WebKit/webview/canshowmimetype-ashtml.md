# canShowMIMEType(asHTML:)

**Framework**: Webkit  
**Kind**: method

Returns whether the receiver interprets a MIME type as HTML.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func canShowMIMEType(asHTML MIMEType: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver interprets `MIMEType` as HTML; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `MIMEType`: The MIME type of the content.

## See Also

- [class func canShowMIMEType(String!) -> Bool](webview/canshowmimetype(_:).md)
  Returns whether the receiver can display content of a given MIME type.
- [class func mimeTypesShownAsHTML() -> [Any]!](webview/mimetypesshownashtml.md)
  Returns a list of MIME types that WebKit renders as HTML.
- [class func setMIMETypesShownAsHTML([Any]!)](webview/setmimetypesshownashtml(_:).md)
  Sets the MIME types that WebKit attempts to render as HTML.
- [var supportsTextEncoding: Bool](webview/supportstextencoding.md)
  A Boolean that indicates whether the document view supports different text encodings.
- [var customTextEncodingName: String!](webview/customtextencodingname.md)
  The custom text encoding name.
- [var textSizeMultiplier: Float](webview/textsizemultiplier.md)
  The font size multiplier for text displayed in web frame view objects managed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/canshowmimetype(ashtml:))*