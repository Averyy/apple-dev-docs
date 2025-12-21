# webView(_:shouldPerformAction:fromSender:)

**Framework**: WebKit  
**Kind**: method

Returns a Boolean value that indicates whether the action sent by the specified object should be performed.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldPerformAction action: Selector!, fromSender sender: Any!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action should be performed; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method allows the delegate to control the web view’s behavior when action methods are invoked. For example, if the action is `copy:`, the delegate can return [`false`](https://developer.apple.com/documentation/Swift/false) to perform a copy in some other way than the default.

## Parameters

- `webView`: The web view that sent the message.
- `action`: The action to perform. See   for information on actions a web view can perform.
- `sender`: The object that sent the action.

## See Also

- [func webView(WebView!, validate: (any NSValidatedUserInterfaceItem)!, defaultValidation: Bool) -> Bool](webuidelegate/webview(_:validate:defaultvalidation:).md)
  Returns a Boolean value that indicates whether the specified user interface item is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:shouldperformaction:fromsender:))*