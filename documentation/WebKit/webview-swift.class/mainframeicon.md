# mainFrameIcon

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The site’s favicon.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var mainFrameIcon: NSImage! { get }
```

```objc
@property (nonatomic, strong, readonly) NSImage * mainFrameIcon;
```

## See Also

### Getting and Setting Frame Contents
- [var isLoading: Bool](./isloading.md)
  A Boolean that indicates whether the web view is loading content.
- [var selectedFrame: WebFrame!](./selectedframe.md)
  The frame with the active selection.
- [var mainFrameURL: String!](./mainframeurl.md)
  The URL that the main frame loads.
- [var mainFrameTitle: String!](./mainframetitle.md)
  The HTML title of the loaded page.
- [var mainFrameDocument: DOMDocument!](./mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/mainframeicon)*