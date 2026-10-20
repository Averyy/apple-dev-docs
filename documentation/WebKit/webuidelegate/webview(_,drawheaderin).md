# webView(_:drawHeaderIn:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Draws the web view’s header in the specified rectangle.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, drawHeaderIn rect: NSRect)
```

```objc
- (void) webView:(WebView *) sender drawHeaderInRect:(NSRect) rect;
```

## Parameters

- `sender`: The web view that sent the message.
- `rect`: The rectangle reserved for drawing the header.

## See Also

### Printing
- [func webView(WebView!, print: WebFrameView!)](./webview%28_,print%29.md)
  Prints the contents of a web frame view.
- [func webViewHeaderHeight(WebView!) -> Float](./webviewheaderheight%28_%29.md)
  Returns the height of the web view’s printed page header.
- [func webViewFooterHeight(WebView!) -> Float](./webviewfooterheight%28_%29.md)
  Returns the height of the web view’s printed page footer.
- [func webView(WebView!, drawFooterIn: NSRect)](./webview%28_,drawfooterin%29.md)
  Draws the web view’s footer in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:drawheaderin:))*