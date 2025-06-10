# webView(_:runOpenPanelForFileButtonWith:allowMultipleFiles:)

**Framework**: WebKit  
**Kind**: method

Displays an open panel for a file input control.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func webView(_ sender: WebView!, runOpenPanelForFileButtonWith resultListener: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)
```

## Parameters

- `sender`: The web view that sent the message.
- `resultListener`: See the   protocol for how to set these values.
- `allowMultipleFiles`: If  , the open panel should allow multiple files to be selected; otherwise, it should not.

## See Also

- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](webuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedby:).md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedby:).md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](webuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedby:).md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runbeforeunloadconfirmpanelwithmessage:initiatedby:).md)
  Displays a confirmation panel containing the specified message before a window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runopenpanelforfilebuttonwith:allowmultiplefiles:))*