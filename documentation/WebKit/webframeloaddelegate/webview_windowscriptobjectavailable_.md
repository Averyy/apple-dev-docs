# webView:windowScriptObjectAvailable:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Called when a frame’s scripting object for a page is available. Use the [`webView(_:didClearWindowObject:for:)`](./webview%28_,didclearwindowobject,for%29.md) method instead.

**Availability**:
- macOS 10.4+ - Deprecated in 10.5

## Declaration

```objc
- (void) webView:(WebView *) webView windowScriptObjectAvailable:(WebScriptObject *) windowScriptObject;
```

## Discussion

This method is invoked before the page is actually loaded.

## Parameters

- `webView`: The web view containing the frame.
- `windowScriptObject`: The window object in the scripting environment.

## See Also

### Related Documentation
- [var windowScriptObject: WebScriptObject!](../webview-swift.class/windowscriptobject.md)
  The receiver’s window object from the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeloaddelegate/webview:windowscriptobjectavailable:)*