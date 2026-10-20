# webView(_:shouldPerformAction:fromSender:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the action sent by the specified object should be performed.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, shouldPerformAction action: Selector!, fromSender sender: Any!) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView shouldPerformAction:(SEL) action fromSender:(id) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if the action should be performed; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method allows the delegate to control the web view’s behavior when action methods are invoked. For example, if the action is `copy:`, the delegate can return [`false`](../../Swift/false.md) to perform a copy in some other way than the default.

## Parameters

- `webView`: The web view that sent the message.
- `action`: The action to perform. See [`WebView`](../webview-swift.class.md) for information on actions a web view can perform.
- `sender`: The object that sent the action.

## See Also

### Controlling Other Behaviors
- [func webView(WebView!, validate: (any NSValidatedUserInterfaceItem)!, defaultValidation: Bool) -> Bool](./webview%28_,validate,defaultvalidation%29.md)
  Returns a Boolean value that indicates whether the specified user interface item is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:shouldperformaction:fromsender:))*