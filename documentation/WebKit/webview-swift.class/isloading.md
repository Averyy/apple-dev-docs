# isLoading

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the web view is loading content.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var isLoading: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLoading) BOOL loading;
```

#### Discussion

[`true`](../../Swift/true.md) if the web view is currently loading any resources; otherwise, [`false`](../../Swift/false.md).

## See Also

### Getting and Setting Frame Contents
- [var selectedFrame: WebFrame!](./selectedframe.md)
  The frame with the active selection.
- [var mainFrameURL: String!](./mainframeurl.md)
  The URL that the main frame loads.
- [var mainFrameTitle: String!](./mainframetitle.md)
  The HTML title of the loaded page.
- [var mainFrameIcon: NSImage!](./mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](./mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/isloading)*