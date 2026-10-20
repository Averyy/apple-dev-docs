# webView(_:didCommit:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the web view has started to receive content for the main frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, didCommit navigation: WKNavigation!)
```

```objc
- (void) webView:(WKWebView *) webView didCommitNavigation:(WKNavigation *) navigation;
```

#### Discussion

After the navigation delegate’s [`webView(_:decidePolicyFor:decisionHandler:)`](./webview%28_,decidepolicyfor,decisionhandler%29-19mn2.md) method approves the navigation response, the web view begins processing it. As changes become ready, the web view calls this method immediately before it starts to update the main frame.

## Parameters

- `webView`: The web view that is loading the content.
- `navigation`: The navigation object that uniquely identifies the load request.

## See Also

### Tracking the load progress of a request
- [func webView(WKWebView, didStartProvisionalNavigation: WKNavigation!)](./webview%28_,didstartprovisionalnavigation%29.md)
  Tells the delegate that navigation from the main frame has started.
- [func webView(WKWebView, didReceiveServerRedirectForProvisionalNavigation: WKNavigation!)](./webview%28_,didreceiveserverredirectforprovisionalnavigation%29.md)
  Tells the delegate that the web view received a server redirect for a request.
- [func webView(WKWebView, didFinish: WKNavigation!)](./webview%28_,didfinish%29.md)
  Tells the delegate that navigation is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:didcommit:))*