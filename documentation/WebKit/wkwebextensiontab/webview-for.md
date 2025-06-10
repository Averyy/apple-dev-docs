# webView(for:)

**Framework**: WebKit  
**Kind**: method

Called when the web view for the tab is needed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
optional func webView(for context: WKWebExtensionContext) -> WKWebView?
```

#### Discussion

The web view’s [`WKWebViewConfiguration`](wkwebviewconfiguration.md) must have its [`webExtensionController`](wkwebviewconfiguration/webextensioncontroller.md) property set to match the controller of the given context; otherwise `nil` will be used. Defaults to `nil` if not implemented. If `nil`, some critical features will not be available for this tab, such as content injection or modification.

## Parameters

- `context`: The context in which the web extension is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensiontab/webview(for:))*