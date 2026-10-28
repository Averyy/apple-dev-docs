# webView(_:didFinishLoadFor:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when a page load completes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, didFinishLoadFor frame: WebFrame!)
```

```objc
- (void) webView:(WebView *) sender didFinishLoadForFrame:(WebFrame *) frame;
```

## Discussion

This method is invoked when a location request for `frame` has completed; that is, when all the resources are done loading. Additional information about the request can be obtained from the data source of `frame`.

## Parameters

- `sender`: The web view containing the frame.
- `frame`: The frame being loaded.

## See Also

### Related Documentation
- [func webView(WebView!, didStartProvisionalLoadFor: WebFrame!)](./webview%28_,didstartprovisionalloadfor%29.md)
  Called when a page load is in progress in a given frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didfinishloadfor:))*