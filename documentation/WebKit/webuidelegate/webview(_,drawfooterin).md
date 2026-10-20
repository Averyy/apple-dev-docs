# webView(_:drawFooterIn:)

**Framework**: WebKit  
**Kind**: method

Draws the web view’s footer in the specified rectangle.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, drawFooterIn rect: NSRect)
```

## Parameters

- `sender`: The web view that sent the message.
- `rect`: The rectangle reserved for drawing the footer.

## See Also

- [func webView(WebView!, print: WebFrameView!)](webuidelegate/webview(_:print:).md)
  Prints the contents of a web frame view.
- [func webViewHeaderHeight(WebView!) -> Float](webuidelegate/webviewheaderheight(_:).md)
  Returns the height of the web view’s printed page header.
- [func webViewFooterHeight(WebView!) -> Float](webuidelegate/webviewfooterheight(_:).md)
  Returns the height of the web view’s printed page footer.
- [func webView(WebView!, drawHeaderIn: NSRect)](webuidelegate/webview(_:drawheaderin:).md)
  Draws the web view’s header in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:drawfooterin:))*