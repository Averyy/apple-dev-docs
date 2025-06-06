# webView(_:didCreateJavaScriptContext:for:)

**Framework**: Webkit  
**Kind**: method

Notifies the delegate that a new JavaScript context has been created.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, didCreateJavaScriptContext context: JSContext!, for frame: WebFrame!)
```

#### Discussion

If a delegate implements this method along with either [`webView(_:didClearWindowObject:for:)`](webframeloaddelegate/webview(_:didclearwindowobject:for:).md) or [`webView:windowScriptObjectAvailable:`](webframeloaddelegate/webview:windowscriptobjectavailable:.md), only `webView:didCreateJavaScriptContext:forFrame:` will be invoked. This lets the delegate implement multiple versions to maintain backwards compatibility with older versions of WebKit.

## Parameters

- `webView`: The view sending the message.
- `context`: The   representing the frame’s JavaScript window object.
- `frame`: The   to which the context belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didcreatejavascriptcontext:for:))*