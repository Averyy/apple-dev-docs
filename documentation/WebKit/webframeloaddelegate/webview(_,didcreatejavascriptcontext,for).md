# webView(_:didCreateJavaScriptContext:for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that a new JavaScript context has been created.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, didCreateJavaScriptContext context: JSContext!, for frame: WebFrame!)
```

```objc
- (void) webView:(WebView *) webView didCreateJavaScriptContext:(JSContext *) context forFrame:(WebFrame *) frame;
```

## Discussion

If a delegate implements this method along with either [`webView(_:didClearWindowObject:for:)`](./webview%28_,didclearwindowobject,for%29.md) or [`webView:windowScriptObjectAvailable:`](./webview_windowscriptobjectavailable_.md), only `webView:didCreateJavaScriptContext:forFrame:` will be invoked. This lets the delegate implement multiple versions to maintain backwards compatibility with older versions of WebKit.

## Parameters

- `webView`: The view sending the message.
- `context`: The [`JSContext`](../../JavaScriptCore/jscontext.md) representing the frame’s JavaScript window object.
- `frame`: The [`WebFrame`](../webframe.md) to which the context belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview(_:didcreatejavascriptcontext:for:))*