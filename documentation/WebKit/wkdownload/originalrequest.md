# originalRequest

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

An object that represents the request that initiated the download.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
var originalRequest: URLRequest? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSURLRequest * originalRequest;
```

## See Also

### Inspecting the download
- [var webView: WKWebView?](./webview.md)
  The web view where the download initiated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownload/originalrequest)*