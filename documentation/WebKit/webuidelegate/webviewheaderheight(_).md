# webViewHeaderHeight(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the height of the web view’s printed page header.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewHeaderHeight(_ sender: WebView!) -> Float
```

```objc
- (float) webViewHeaderHeight:(WebView *) sender;
```

## Return Value

The height of the web view’s printed page header. Returns `0.0` if no space is reserved for the header.

## Discussion

The height returned by this method is used to calculate the rectangle passed to the [`webView(_:drawHeaderIn:)`](./webview%28_,drawheaderin%29.md) method.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Printing
- [func webView(WebView!, print: WebFrameView!)](./webview%28_,print%29.md)
  Prints the contents of a web frame view.
- [func webViewFooterHeight(WebView!) -> Float](./webviewfooterheight%28_%29.md)
  Returns the height of the web view’s printed page footer.
- [func webView(WebView!, drawHeaderIn: NSRect)](./webview%28_,drawheaderin%29.md)
  Draws the web view’s header in the specified rectangle.
- [func webView(WebView!, drawFooterIn: NSRect)](./webview%28_,drawfooterin%29.md)
  Draws the web view’s footer in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewheaderheight(_:))*