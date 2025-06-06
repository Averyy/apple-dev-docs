# webView(_:didFailLoadWithError:)

**Framework**: UIKit  
**Kind**: method

Sent if a web view failed to load a frame.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: UIWebView, didFailLoadWithError error: any Error)
```

## Parameters

- `webView`: The web view that failed to load a frame.
- `error`: The error that occurred during loading.

## See Also

- [func webView(UIWebView, shouldStartLoadWith: URLRequest, navigationType: UIWebView.NavigationType) -> Bool](uiwebviewdelegate/webview(_:shouldstartloadwith:navigationtype:).md)
  Sent before a web view begins loading a frame.
- [func webViewDidStartLoad(UIWebView)](uiwebviewdelegate/webviewdidstartload(_:).md)
  Sent after a web view starts loading a frame.
- [func webViewDidFinishLoad(UIWebView)](uiwebviewdelegate/webviewdidfinishload(_:).md)
  Sent after a web view finishes loading a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webview(_:didfailloadwitherror:))*