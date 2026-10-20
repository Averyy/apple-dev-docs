# webView(_:didReceiveServerRedirectForProvisionalLoadFor:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when a provisional data source for a frame receives a server redirect.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, didReceiveServerRedirectForProvisionalLoadFor frame: WebFrame!)
```

```objc
- (void) webView:(WebView *) sender didReceiveServerRedirectForProvisionalLoadForFrame:(WebFrame *) frame;
```

#### Discussion

A *server redirect* is when one URL location is redirected to another. Additional information about the new request can be obtained from the data source of `frame`.

## Parameters

- `sender`: The web view containing the frame.
- `frame`: The frame being loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didreceiveserverredirectforprovisionalloadfor:))*