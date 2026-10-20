# webViewDidStartLoad(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent after a web view starts loading a frame.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0

> **Deprecated**: For more information, see [`UIWebView`](../uiwebview.md).

## Declaration

```swift
optional func webViewDidStartLoad(_ webView: UIWebView)
```

```objc
- (void) webViewDidStartLoad:(UIWebView *) webView;
```

## Parameters

- `webView`: The web view that has begun loading a new frame.

## See Also

### Deprecated
- [func webView(UIWebView, shouldStartLoadWith: URLRequest, navigationType: UIWebView.NavigationType) -> Bool](./webview%28_,shouldstartloadwith,navigationtype%29.md)
  Sent before a web view begins loading a frame.
- [func webViewDidFinishLoad(UIWebView)](./webviewdidfinishload%28_%29.md)
  Sent after a web view finishes loading a frame.
- [func webView(UIWebView, didFailLoadWithError: any Error)](./webview%28_,didfailloadwitherror%29.md)
  Sent if a web view failed to load a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwebviewdelegate/webviewdidstartload(_:))*