# webView(_:runBeforeUnloadConfirmPanelWithMessage:initiatedBy:)

**Framework**: WebKit  
**Kind**: method

Displays a confirmation panel containing the specified message before a window closes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, runBeforeUnloadConfirmPanelWithMessage message: String!, initiatedBy frame: WebFrame!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the user clicked the OK button; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Use this method to include a message in the confirmation panel in addition to the message supplied by the webpage. The confirmation panel should contain OK and Cancel buttons.

## Parameters

- `sender`: The web view that sent the message.
- `message`: The message to display in the panel.
- `frame`: The web frame whose JavaScript initiated this call.

## See Also

- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](webuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedby:).md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedby:).md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](webuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedby:).md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:allowmultiplefiles:).md)
  Displays an open panel for a file input control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runbeforeunloadconfirmpanelwithmessage:initiatedby:))*