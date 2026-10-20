# webView(_:validate:defaultValidation:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the specified user interface item is valid.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, validate item: (any NSValidatedUserInterfaceItem)!, defaultValidation: Bool) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView validateUserInterfaceItem:(id<NSValidatedUserInterfaceItem>) item defaultValidation:(BOOL) defaultValidation;
```

#### Return Value

[`true`](../../Swift/true.md) if the specified user interface item is valid; otherwise, [`false`](../../Swift/false.md).

#### Discussion

See [`NSUserInterfaceValidations`](../../AppKit/nsuserinterfacevalidations.md) and [`NSValidatedUserInterfaceItem`](../../AppKit/nsvalidateduserinterfaceitem.md) for more information about user interface validation. If you do not implement this method, the value of `defaultValidation` is used.

## Parameters

- `webView`: The web view that sent the message.
- `item`: The user interface item being validated.
- `defaultValidation`: [`true`](../../Swift/true.md) if the web view believes the user interface item is valid; otherwise, [`false`](../../Swift/false.md).

## See Also

### Controlling Other Behaviors
- [func webView(WebView!, shouldPerformAction: Selector!, fromSender: Any!) -> Bool](./webview%28_,shouldperformaction,fromsender%29.md)
  Returns a Boolean value that indicates whether the action sent by the specified object should be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:validate:defaultvalidation:))*