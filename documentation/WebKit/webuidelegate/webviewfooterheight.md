# webViewFooterHeight(_:)

**Framework**: WebKit  
**Kind**: method

Returns the height of the web view’s printed page footer.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webViewFooterHeight(_ sender: WebView!) -> Float
```

#### Return Value

The height of the web view’s printed page footer. Returns `0.0` if no space is reserved for the footer.

#### Discussion

The height returned by this method is used to calculate the rectangle passed to the [`webView(_:drawFooterIn:)`](webuidelegate/webview(_:drawfooterin:).md) method.

## Parameters

- `sender`: The web view that sent the message.

## See Also

- [func webView(WebView!, print: WebFrameView!)](webuidelegate/webview(_:print:).md)
  Prints the contents of a web frame view.
- [func webViewHeaderHeight(WebView!) -> Float](webuidelegate/webviewheaderheight(_:).md)
  Returns the height of the web view’s printed page header.
- [func webView(WebView!, drawHeaderIn: NSRect)](webuidelegate/webview(_:drawheaderin:).md)
  Draws the web view’s header in the specified rectangle.
- [func webView(WebView!, drawFooterIn: NSRect)](webuidelegate/webview(_:drawfooterin:).md)
  Draws the web view’s footer in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewfooterheight(_:))*