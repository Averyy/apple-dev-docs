# webView(_:didCancelClientRedirectFor:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when a client redirect is cancelled.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, didCancelClientRedirectFor frame: WebFrame!)
```

```objc
- (void) webView:(WebView *) sender didCancelClientRedirectForFrame:(WebFrame *) frame;
```

#### Discussion

This might happen if a frame changes locations before a pending client redirect is fired. The client redirect occurred in `frame`.

## Parameters

- `sender`: The web view containing the frame.
- `frame`: The frame being loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didcancelclientredirectfor:))*