# mainFrameTitle

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The HTML title of the loaded page.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var mainFrameTitle: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * mainFrameTitle;
```

#### Discussion

The HTML title of the loaded page. Returns `@""` if the loaded document is not HTML.

## See Also

### Getting and Setting Frame Contents
- [var isLoading: Bool](./isloading.md)
  A Boolean that indicates whether the web view is loading content.
- [var selectedFrame: WebFrame!](./selectedframe.md)
  The frame with the active selection.
- [var mainFrameURL: String!](./mainframeurl.md)
  The URL that the main frame loads.
- [var mainFrameIcon: NSImage!](./mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](./mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/mainframetitle)*