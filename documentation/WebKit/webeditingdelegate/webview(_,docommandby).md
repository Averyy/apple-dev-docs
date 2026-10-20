# webView(_:doCommandBy:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the receiver performs a command instead of the web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ webView: WebView!, doCommandBy selector: Selector!) -> Bool
```

```objc
- (BOOL) webView:(WebView *) webView doCommandBySelector:(SEL) selector;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver will perform `command`; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Implement this method if you want to perform `command` instead of letting the web view perform `command`.

## Parameters

- `webView`: The web view that the user is editing.
- `selector`: The command to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/webview(_:docommandby:))*