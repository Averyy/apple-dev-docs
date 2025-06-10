# webView(_:doCommandBy:)

**Framework**: WebKit  
**Kind**: method

Returns whether the receiver performs a command instead of the web view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ webView: WebView!, doCommandBy selector: Selector!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver will perform `command`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Implement this method if you want to perform `command` instead of letting the web view perform `command`.

## Parameters

- `webView`: The web view that the user is editing.
- `selector`: The command to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:docommandby:))*