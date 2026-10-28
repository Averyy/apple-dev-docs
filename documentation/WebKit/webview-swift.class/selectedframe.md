# selectedFrame

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The frame with the active selection.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var selectedFrame: WebFrame! { get }
```

```objc
@property (nonatomic, strong, readonly) WebFrame * selectedFrame;
```

## Discussion

If it doesn’t exist, the frame that contains a non-zero-length selection; otherwise, `nil`.

## See Also

### Getting and Setting Frame Contents
- [var isLoading: Bool](./isloading.md)
  A Boolean that indicates whether the web view is loading content.
- [var mainFrameURL: String!](./mainframeurl.md)
  The URL that the main frame loads.
- [var mainFrameTitle: String!](./mainframetitle.md)
  The HTML title of the loaded page.
- [var mainFrameIcon: NSImage!](./mainframeicon.md)
  The site’s favicon.
- [var mainFrameDocument: DOMDocument!](./mainframedocument.md)
  The DOM document for the main frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/selectedframe)*