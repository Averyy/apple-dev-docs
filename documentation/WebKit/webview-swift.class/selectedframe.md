# selectedFrame

**Framework**: WebKit  
**Kind**: property

The frame with the active selection.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var selectedFrame: WebFrame! { get }
```

#### Discussion

If it doesn’t exist, the frame that contains a non-zero-length selection; otherwise, `nil`.

## See Also

- [var isLoading: Bool](webview-swift.class/isloading.md)
  A Boolean that indicates whether the web view is loading content.
- [var mainFrameURL: String!](webview-swift.class/mainframeurl.md)
  The URL that the main frame loads.
- [var mainFrameTitle: String!](webview-swift.class/mainframetitle.md)
  The HTML title of the loaded page.
- [var mainFrameIcon: NSImage!](webview-swift.class/mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](webview-swift.class/mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/selectedframe)*