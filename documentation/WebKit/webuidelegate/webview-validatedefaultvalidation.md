# webView(_:validate:defaultValidation:)

**Framework**: WebKit  
**Kind**: method

Returns a Boolean value that indicates whether the specified user interface item is valid.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, validate item: (any NSValidatedUserInterfaceItem)!, defaultValidation: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the specified user interface item is valid; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

See [`NSUserInterfaceValidations`](https://developer.apple.com/documentation/AppKit/NSUserInterfaceValidations) and [`NSValidatedUserInterfaceItem`](https://developer.apple.com/documentation/AppKit/NSValidatedUserInterfaceItem) for more information about user interface validation. If you do not implement this method, the value of `defaultValidation` is used.

## Parameters

- `webView`: The web view that sent the message.
- `item`: The user interface item being validated.
- `defaultValidation`:   if the web view believes the user interface item is valid; otherwise,  .

## See Also

- [func webView(WebView!, shouldPerformAction: Selector!, fromSender: Any!) -> Bool](webuidelegate/webview(_:shouldperformaction:fromsender:).md)
  Returns a Boolean value that indicates whether the action sent by the specified object should be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:validate:defaultvalidation:))*