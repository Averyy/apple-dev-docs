# webViewStatusText(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the current status message from a web view’s window.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webViewStatusText(_ sender: WebView!) -> String!
```

```objc
- (NSString *) webViewStatusText:(WebView *) sender;
```

#### Return Value

The status message displayed in the web view’s window if one has been set with the [`webView(_:setStatusText:)`](./webview%28_,setstatustext%29.md) method; otherwise, `nil`.

## Parameters

- `sender`: The web view that sent the message.

## See Also

### Displaying Status Messages
- [func webView(WebView!, setStatusText: String!)](./webview%28_,setstatustext%29.md)
  Sets the status message displayed by a web view’s window, if any, to the specified text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webviewstatustext(_:))*