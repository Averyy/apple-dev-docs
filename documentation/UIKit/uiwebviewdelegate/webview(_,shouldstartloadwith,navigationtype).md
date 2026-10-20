# webView(_:shouldStartLoadWith:navigationType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent before a web view begins loading a frame.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
optional func webView(_ webView: UIWebView, shouldStartLoadWith request: URLRequest, navigationType: UIWebView.NavigationType) -> Bool
```

```objc
- (BOOL) webView:(UIWebView *) webView shouldStartLoadWithRequest:(NSURLRequest *) request navigationType:(UIWebViewNavigationType) navigationType;
```

#### Return Value

[`true`](../../Swift/true.md) if the web view should begin loading content; otherwise, [`false`](../../Swift/false.md) .

## Parameters

- `webView`: The web view that is about to load a new frame.
- `request`: The content location.
- `navigationType`: The type of user action that started the load request.

## See Also

### Deprecated
- [func webViewDidStartLoad(UIWebView)](./webviewdidstartload%28_%29.md)
  Sent after a web view starts loading a frame.
- [func webViewDidFinishLoad(UIWebView)](./webviewdidfinishload%28_%29.md)
  Sent after a web view finishes loading a frame.
- [func webView(UIWebView, didFailLoadWithError: any Error)](./webview%28_,didfailloadwitherror%29.md)
  Sent if a web view failed to load a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webview(_:shouldstartloadwith:navigationtype:))*