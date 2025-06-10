# webView(_:runJavaScriptTextInputPanelWithPrompt:defaultText:initiatedBy:)

**Framework**: WebKit  
**Kind**: method

Displays a JavaScript text input panel and returns the entered text.

**Availability**:
- macOS 10.3+

## Declaration

```swift
optional func webView(_ sender: WebView!, runJavaScriptTextInputPanelWithPrompt prompt: String!, defaultText: String!, initiatedBy frame: WebFrame!) -> String!
```

#### Return Value

The text entered by the user if the user clicks OK; otherwise, `nil`.

#### Discussion

This method is used to provide an alternate text input panel when JavaScript code calls `prompt`. Delegates should visually indicate that this panel comes from JavaScript. The panel should contain an OK and a Cancel button, and an editable text field. If you do not implement this method, a JavaScript text input panel is displayed.

## Parameters

- `sender`: The web view that sent the message.
- `prompt`: The message to display in the text input panel.
- `defaultText`: Default placeholder text to display in the text field.
- `frame`: The web frame whose JavaScript initiated this call.

## See Also

- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](webuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedby:).md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedby:).md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](webuidelegate/webview(_:runopenpanelforfilebuttonwith:allowmultiplefiles:).md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](webuidelegate/webview(_:runbeforeunloadconfirmpanelwithmessage:initiatedby:).md)
  Displays a confirmation panel containing the specified message before a window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedby:))*