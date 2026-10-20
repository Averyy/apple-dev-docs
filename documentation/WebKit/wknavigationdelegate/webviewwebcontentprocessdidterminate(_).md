# webViewWebContentProcessDidTerminate(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the web view’s content process was terminated.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
optional func webViewWebContentProcessDidTerminate(_ webView: WKWebView)
```

```objc
- (void) webViewWebContentProcessDidTerminate:(WKWebView *) webView;
```

#### Discussion

Web views use a separate process to render and manage web content. WebKit calls this method when the process for the specified web view terminates for any reason.

## Parameters

- `webView`: The web view whose underlying web content process was terminated.

## See Also

### Responding to navigation errors
- [func webView(WKWebView, didFail: WKNavigation!, withError: any Error)](./webview%28_,didfail,witherror%29.md)
  Tells the delegate that an error occurred during navigation.
- [func webView(WKWebView, didFailProvisionalNavigation: WKNavigation!, withError: any Error)](./webview%28_,didfailprovisionalnavigation,witherror%29.md)
  Tells the delegate that an error occurred during the early navigation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webviewwebcontentprocessdidterminate(_:))*