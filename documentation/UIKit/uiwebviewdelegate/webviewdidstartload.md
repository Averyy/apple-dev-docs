# webViewDidStartLoad(_:)

**Framework**: UIKit  
**Kind**: method

Sent after a web view starts loading a frame.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+

## Declaration

```swift
@MainActor
optional func webViewDidStartLoad(_ webView: UIWebView)
```

## Parameters

- `webView`: The web view that has begun loading a new frame.

## See Also

- [func webView(UIWebView, shouldStartLoadWith: URLRequest, navigationType: UIWebView.NavigationType) -> Bool](uiwebviewdelegate/webview(_:shouldstartloadwith:navigationtype:).md)
  Sent before a web view begins loading a frame.
- [func webViewDidFinishLoad(UIWebView)](uiwebviewdelegate/webviewdidfinishload(_:).md)
  Sent after a web view finishes loading a frame.
- [func webView(UIWebView, didFailLoadWithError: any Error)](uiwebviewdelegate/webview(_:didfailloadwitherror:).md)
  Sent if a web view failed to load a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webviewdidstartload(_:))*