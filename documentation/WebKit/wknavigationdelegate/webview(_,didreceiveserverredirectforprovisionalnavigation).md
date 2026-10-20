# webView(_:didReceiveServerRedirectForProvisionalNavigation:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the web view received a server redirect for a request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!)
```

```objc
- (void) webView:(WKWebView *) webView didReceiveServerRedirectForProvisionalNavigation:(WKNavigation *) navigation;
```

## Parameters

- `webView`: The web view that is loading the content.
- `navigation`: The navigation object that received a server redirect.

## See Also

### Tracking the load progress of a request
- [func webView(WKWebView, didStartProvisionalNavigation: WKNavigation!)](./webview%28_,didstartprovisionalnavigation%29.md)
  Tells the delegate that navigation from the main frame has started.
- [func webView(WKWebView, didCommit: WKNavigation!)](./webview%28_,didcommit%29.md)
  Tells the delegate that the web view has started to receive content for the main frame.
- [func webView(WKWebView, didFinish: WKNavigation!)](./webview%28_,didfinish%29.md)
  Tells the delegate that navigation is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:didreceiveserverredirectforprovisionalnavigation:))*