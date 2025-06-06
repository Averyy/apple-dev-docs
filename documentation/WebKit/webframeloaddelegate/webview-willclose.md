# webView(_:willClose:)

**Framework**: Webkit  
**Kind**: method

Called when a frame will be closed.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, willClose frame: WebFrame!)
```

#### Discussion

Called right before WebKit is done with `frame` and the objects it owns.

## Parameters

- `sender`: The web view containing the frame.
- `frame`: The frame being loaded.

## See Also

- [func webView(WebView!, willPerformClientRedirectTo: URL!, delay: TimeInterval, fire: Date!, for: WebFrame!)](webframeloaddelegate/webview(_:willperformclientredirectto:delay:fire:for:).md)
  Called when a frame receives a client redirect and before it is fired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:willclose:))*