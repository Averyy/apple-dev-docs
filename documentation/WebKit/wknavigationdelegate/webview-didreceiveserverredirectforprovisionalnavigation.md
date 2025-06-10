# webView(_:didReceiveServerRedirectForProvisionalNavigation:)

**Framework**: WebKit  
**Kind**: method

Tells the delegate that the web view received a server redirect for a request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, didReceiveServerRedirectForProvisionalNavigation navigation: WKNavigation!)
```

## Parameters

- `webView`: The web view that is loading the content.
- `navigation`: The navigation object that received a server redirect.

## See Also

- [func webView(WKWebView, didStartProvisionalNavigation: WKNavigation!)](wknavigationdelegate/webview(_:didstartprovisionalnavigation:).md)
  Tells the delegate that navigation from the main frame has started.
- [func webView(WKWebView, didCommit: WKNavigation!)](wknavigationdelegate/webview(_:didcommit:).md)
  Tells the delegate that the web view has started to receive content for the main frame.
- [func webView(WKWebView, didFinish: WKNavigation!)](wknavigationdelegate/webview(_:didfinish:).md)
  Tells the delegate that navigation is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:didreceiveserverredirectforprovisionalnavigation:))*