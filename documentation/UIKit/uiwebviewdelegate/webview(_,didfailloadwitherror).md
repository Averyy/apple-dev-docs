# webView(_:didFailLoadWithError:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent if a web view failed to load a frame.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
optional func webView(_ webView: UIWebView, didFailLoadWithError error: any Error)
```

```objc
- (void) webView:(UIWebView *) webView didFailLoadWithError:(NSError *) error;
```

## Parameters

- `webView`: The web view that failed to load a frame.
- `error`: The error that occurred during loading.

## See Also

### Deprecated
- [func webView(UIWebView, shouldStartLoadWith: URLRequest, navigationType: UIWebView.NavigationType) -> Bool](./webview%28_,shouldstartloadwith,navigationtype%29.md)
  Sent before a web view begins loading a frame.
- [func webViewDidStartLoad(UIWebView)](./webviewdidstartload%28_%29.md)
  Sent after a web view starts loading a frame.
- [func webViewDidFinishLoad(UIWebView)](./webviewdidfinishload%28_%29.md)
  Sent after a web view finishes loading a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webview(_:didfailloadwitherror:))*