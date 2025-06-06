# mainFrameTitle

**Framework**: Webkit  
**Kind**: property

The HTML title of the loaded page.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var mainFrameTitle: String! { get }
```

#### Discussion

The HTML title of the loaded page. Returns `@""` if the loaded document is not HTML.

## See Also

- [var isLoading: Bool](webview/isloading.md)
  A Boolean that indicates whether the web view is loading content.
- [var selectedFrame: WebFrame!](webview/selectedframe.md)
  The frame with the active selection.
- [var mainFrameURL: String!](webview/mainframeurl.md)
  The URL that the main frame loads.
- [var mainFrameIcon: NSImage!](webview/mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](webview/mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/mainframetitle)*