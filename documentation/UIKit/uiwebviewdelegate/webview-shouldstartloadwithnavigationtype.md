# webView(_:shouldStartLoadWith:navigationType:)

**Framework**: UIKit  
**Kind**: method

Sent before a web view begins loading a frame.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: UIWebView, shouldStartLoadWith request: URLRequest, navigationType: UIWebView.NavigationType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the web view should begin loading content; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) .

## Parameters

- `webView`: The web view that is about to load a new frame.
- `request`: The content location.
- `navigationType`: The type of user action that started the load request.

## See Also

- [func webViewDidStartLoad(UIWebView)](uiwebviewdelegate/webviewdidstartload(_:).md)
  Sent after a web view starts loading a frame.
- [func webViewDidFinishLoad(UIWebView)](uiwebviewdelegate/webviewdidfinishload(_:).md)
  Sent after a web view finishes loading a frame.
- [func webView(UIWebView, didFailLoadWithError: any Error)](uiwebviewdelegate/webview(_:didfailloadwitherror:).md)
  Sent if a web view failed to load a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webview(_:shouldstartloadwith:navigationtype:))*