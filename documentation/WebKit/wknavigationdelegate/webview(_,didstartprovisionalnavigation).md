# webView(_:didStartProvisionalNavigation:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that navigation from the main frame has started.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, didStartProvisionalNavigation navigation: WKNavigation!)
```

```objc
- (void) webView:(WKWebView *) webView didStartProvisionalNavigation:(WKNavigation *) navigation;
```

## Mentions

- [Replacing UIWebView in your app](../replacing-uiwebview-in-your-app.md)

#### Discussion

The web view calls this method after it receives provisional approval to process a navigation request, but before it receives a response to that request.

## Parameters

- `webView`: The web view that is loading the content.
- `navigation`: The navigation object associated with the load request.

## See Also

### Tracking the load progress of a request
- [func webView(WKWebView, didReceiveServerRedirectForProvisionalNavigation: WKNavigation!)](./webview%28_,didreceiveserverredirectforprovisionalnavigation%29.md)
  Tells the delegate that the web view received a server redirect for a request.
- [func webView(WKWebView, didCommit: WKNavigation!)](./webview%28_,didcommit%29.md)
  Tells the delegate that the web view has started to receive content for the main frame.
- [func webView(WKWebView, didFinish: WKNavigation!)](./webview%28_,didfinish%29.md)
  Tells the delegate that navigation is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:didstartprovisionalnavigation:))*