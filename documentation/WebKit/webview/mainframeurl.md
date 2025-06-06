# mainFrameURL

**Framework**: Webkit  
**Kind**: property

The URL that the main frame loads.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var mainFrameURL: String! { get set }
```

#### Discussion

Functionally equivalent to invoking `[[webView mainFrame] loadRequest:[NSURLRequest requestWithURL: [NSURL URLWithString:URLString]]]`.

## See Also

- [var isLoading: Bool](webview/isloading.md)
  A Boolean that indicates whether the web view is loading content.
- [var selectedFrame: WebFrame!](webview/selectedframe.md)
  The frame with the active selection.
- [var mainFrameTitle: String!](webview/mainframetitle.md)
  The HTML title of the loaded page.
- [var mainFrameIcon: NSImage!](webview/mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](webview/mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/mainframeurl)*