# webView(_:runOpenPanelForFileButtonWith:)

**Framework**: WebKit  
**Kind**: method

Displays an open panel for a file input control.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, runOpenPanelForFileButtonWith resultListener: (any WebOpenPanelResultListener)!)
```

#### Discussion

This method uses a listener object to set the results of the open panel, instead of returning the value directly. This approach allows delegates to implement the open panel as a modal dialog. No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `resultListener`: See the   protocol for how to set these values.

## See Also

- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](webuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedby:).md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedby:).md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](webuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedby:).md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:allowmultiplefiles:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runbeforeunloadconfirmpanelwithmessage:initiatedby:).md)
  Displays a confirmation panel containing the specified message before a window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runopenpanelforfilebuttonwith:))*