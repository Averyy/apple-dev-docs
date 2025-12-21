# webView(_:runJavaScriptConfirmPanelWithMessage:initiatedBy:)

**Framework**: WebKit  
**Kind**: method

Displays a JavaScript confirmation panel with the specified message.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, runJavaScriptConfirmPanelWithMessage message: String!, initiatedBy frame: WebFrame!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the user clicks OK; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method displays a confirmation panel when JavaScript code calls `confirm`. Delegates should visually indicate that this panel comes from JavaScript. The panel should contain an OK and a Cancel button. No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `message`: The message to display in the confirmation panel.
- `frame`: The web frame whose JavaScript initiated this call.

## See Also

- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](webuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedby:).md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](webuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedby:).md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:allowmultiplefiles:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runbeforeunloadconfirmpanelwithmessage:initiatedby:).md)
  Displays a confirmation panel containing the specified message before a window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedby:))*