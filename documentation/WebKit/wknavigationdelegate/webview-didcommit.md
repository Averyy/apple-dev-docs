# webView(_:didCommit:)

**Framework**: Webkit  
**Kind**: method

Tells the delegate that the web view has started to receive content for the main frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, didCommit navigation: WKNavigation!)
```

#### Discussion

After the navigation delegate’s [`webView(_:decidePolicyFor:decisionHandler:)`](wknavigationdelegate/webview(_:decidepolicyfor:decisionhandler:)-19mn2.md) method approves the navigation response, the web view begins processing it. As changes become ready, the web view calls this method immediately before it starts to update the main frame.

## Parameters

- `webView`: The web view that is loading the content.
- `navigation`: The navigation object that uniquely identifies the load request.

## See Also

- [func webView(WKWebView, didStartProvisionalNavigation: WKNavigation!)](wknavigationdelegate/webview(_:didstartprovisionalnavigation:).md)
  Tells the delegate that navigation from the main frame has started.
- [func webView(WKWebView, didReceiveServerRedirectForProvisionalNavigation: WKNavigation!)](wknavigationdelegate/webview(_:didreceiveserverredirectforprovisionalnavigation:).md)
  Tells the delegate that the web view received a server redirect for a request.
- [func webView(WKWebView, didFinish: WKNavigation!)](wknavigationdelegate/webview(_:didfinish:).md)
  Tells the delegate that navigation is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:didcommit:))*