# webView(_:runJavaScriptAlertPanelWithMessage:initiatedBy:)

**Framework**: WebKit  
**Kind**: method

Displays a JavaScript alert panel containing the specified message.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, runJavaScriptAlertPanelWithMessage message: String!, initiatedBy frame: WebFrame!)
```

#### Discussion

This method displays an alert panel when JavaScript code calls `alert`. Delegates should visually indicate that this panel comes from JavaScript. The panel should contain a single OK button. No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `message`: The message to display in the alert panel.
- `frame`: The web frame whose JavaScript initiated this call.

## See Also

- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedby:).md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](webuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedby:).md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:allowmultiplefiles:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runbeforeunloadconfirmpanelwithmessage:initiatedby:).md)
  Displays a confirmation panel containing the specified message before a window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedby:))*