# setMIMETypesShownAsHTML(_:)

**Framework**: WebKit  
**Kind**: method

Sets the MIME types that WebKit attempts to render as HTML.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class func setMIMETypesShownAsHTML(_ MIMETypes: [Any]!)
```

## Parameters

- `MIMETypes`: An array of   objects representing the MIME types. Typically, you create the   array by adding additional types to the array returned by the   class method.

## See Also

- [class func canShowMIMEType(String!) -> Bool](webview-swift.class/canshowmimetype(_:).md)
  Returns whether the receiver can display content of a given MIME type.
- [class func mimeTypesShownAsHTML() -> [Any]!](webview-swift.class/mimetypesshownashtml.md)
  Returns a list of MIME types that WebKit renders as HTML.
- [class func canShowMIMEType(asHTML: String!) -> Bool](webview-swift.class/canshowmimetype(ashtml:).md)
  Returns whether the receiver interprets a MIME type as HTML.
- [var supportsTextEncoding: Bool](webview-swift.class/supportstextencoding.md)
  A Boolean that indicates whether the document view supports different text encodings.
- [var customTextEncodingName: String!](webview-swift.class/customtextencodingname.md)
  The custom text encoding name.
- [var textSizeMultiplier: Float](webview-swift.class/textsizemultiplier.md)
  The font size multiplier for text displayed in web frame view objects managed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/setmimetypesshownashtml(_:))*