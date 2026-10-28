# textSizeMultiplier

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The font size multiplier for text displayed in web frame view objects managed by the receiver.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var textSizeMultiplier: Float { get set }
```

```objc
@property (nonatomic) float textSizeMultiplier;
```

## Discussion

Measured as a fractional percentage value where `1.0` denotes 100%.

## See Also

### Getting and Setting Content Information
- [class func canShowMIMEType(String!) -> Bool](./canshowmimetype%28_%29.md)
  Returns whether the receiver can display content of a given MIME type.
- [class func mimeTypesShownAsHTML() -> [Any]!](./mimetypesshownashtml%28%29.md)
  Returns a list of MIME types that WebKit renders as HTML.
- [class func setMIMETypesShownAsHTML([Any]!)](./setmimetypesshownashtml%28_%29.md)
  Sets the MIME types that WebKit attempts to render as HTML.
- [class func canShowMIMEType(asHTML: String!) -> Bool](./canshowmimetype%28ashtml%29.md)
  Returns whether the receiver interprets a MIME type as HTML.
- [var supportsTextEncoding: Bool](./supportstextencoding.md)
  A Boolean that indicates whether the document view supports different text encodings.
- [var customTextEncodingName: String!](./customtextencodingname.md)
  The custom text encoding name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/textsizemultiplier)*