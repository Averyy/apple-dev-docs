# webView:runJavaScriptConfirmPanelWithMessage:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays a JavaScript confirm panel.

**Availability**:
- macOS 10.3+ - Deprecated in 10.5

> **Deprecated**: Use webView:runJavaScriptConfirmPanelWithMessage:initiatedByFrame: instead.

## Declaration

```objc
- (BOOL) webView:(WebView *) sender runJavaScriptConfirmPanelWithMessage:(NSString *) message;
```

#### Discussion

This method is used to display a confirmation panel when JavaScript code calls `confirm`. It returns [`true`](../../Swift/true.md) if confirmed, [`false`](../../Swift/false.md) otherwise. Delegates should visually indicate that this panel comes from JavaScript. The panel should have, for example, an OK and Cancel button. No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `message`: The message to display in the confirmation panel.

## See Also

### Opening Panels
- [- webView:runJavaScriptAlertPanelWithMessage:](./webview_runjavascriptalertpanelwithmessage_.md)
  Displays a JavaScript alert panel.
- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](./webview%28_,runjavascriptalertpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](./webview%28_,runjavascriptconfirmpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript confirmation panel with the specified message.
- [- webView:runJavaScriptTextInputPanelWithPrompt:defaultText:](./webview_runjavascripttextinputpanelwithprompt_defaulttext_.md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](./webview%28_,runjavascripttextinputpanelwithprompt,defaulttext,initiatedby%29.md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](./webview%28_,runopenpanelforfilebuttonwith%29.md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](./webview%28_,runopenpanelforfilebuttonwith,allowmultiplefiles%29.md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](./webview%28_,runbeforeunloadconfirmpanelwithmessage,initiatedby%29.md)
  Displays a confirmation panel containing the specified message before a window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview:runjavascriptconfirmpanelwithmessage:)*