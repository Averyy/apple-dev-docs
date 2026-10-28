# webView(_:setStatusText:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the status message displayed by a web view’s window, if any, to the specified text.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, setStatusText text: String!)
```

```objc
- (void) webView:(WebView *) sender setStatusText:(NSString *) text;
```

## Discussion

The delegate receives this message when a JavaScript function in the web view explicitly sets the status text. No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `text`: The status message to display.

## See Also

### Displaying Status Messages
- [func webViewStatusText(WebView!) -> String!](./webviewstatustext%28_%29.md)
  Returns the current status message from a web view’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:setstatustext:))*