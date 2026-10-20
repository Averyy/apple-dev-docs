# mainFrameURL

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The URL that the main frame loads.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var mainFrameURL: String! { get set }
```

```objc
@property (nonatomic, copy) NSString * mainFrameURL;
```

#### Discussion

Functionally equivalent to invoking `[[webView mainFrame] loadRequest:[NSURLRequest requestWithURL: [NSURL URLWithString:URLString]]]`.

## See Also

### Getting and Setting Frame Contents
- [var isLoading: Bool](./isloading.md)
  A Boolean that indicates whether the web view is loading content.
- [var selectedFrame: WebFrame!](./selectedframe.md)
  The frame with the active selection.
- [var mainFrameTitle: String!](./mainframetitle.md)
  The HTML title of the loaded page.
- [var mainFrameIcon: NSImage!](./mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](./mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/mainframeurl)*