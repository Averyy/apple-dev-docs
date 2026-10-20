# webView

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The web view where the download initiated.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
weak var webView: WKWebView? { get }
```

```objc
@property (nonatomic, weak, readonly) WKWebView * webView;
```

## See Also

### Inspecting the download
- [var originalRequest: URLRequest?](./originalrequest.md)
  An object that represents the request that initiated the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload/webview)*