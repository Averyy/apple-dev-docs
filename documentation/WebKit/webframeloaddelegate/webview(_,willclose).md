# webView(_:willClose:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when a frame will be closed.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, willClose frame: WebFrame!)
```

```objc
- (void) webView:(WebView *) sender willCloseFrame:(WebFrame *) frame;
```

## Discussion

Called right before WebKit is done with `frame` and the objects it owns.

## Parameters

- `sender`: The web view containing the frame.
- `frame`: The frame being loaded.

## See Also

### Related Documentation
- [func webView(WebView!, willPerformClientRedirectTo: URL!, delay: TimeInterval, fire: Date!, for: WebFrame!)](./webview%28_,willperformclientredirectto,delay,fire,for%29.md)
  Called when a frame receives a client redirect and before it is fired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:willclose:))*