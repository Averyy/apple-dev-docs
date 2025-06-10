# isLoading

**Framework**: WebKit  
**Kind**: property

A Boolean that indicates whether the web view is loading content.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var isLoading: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the web view is currently loading any resources; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var selectedFrame: WebFrame!](webview-swift.class/selectedframe.md)
  The frame with the active selection.
- [var mainFrameURL: String!](webview-swift.class/mainframeurl.md)
  The URL that the main frame loads.
- [var mainFrameTitle: String!](webview-swift.class/mainframetitle.md)
  The HTML title of the loaded page.
- [var mainFrameIcon: NSImage!](webview-swift.class/mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](webview-swift.class/mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/isloading)*