# webView:runJavaScriptAlertPanelWithMessage:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays a JavaScript alert panel.

**Availability**:
- macOS 10.3+ - Deprecated in 10.5

> **Deprecated**: Use webView:runJavaScriptAlertPanelWithMessage:initiatedByFrame: instead.

## Declaration

```objc
- (void) webView:(WebView *) sender runJavaScriptAlertPanelWithMessage:(NSString *) message;
```

#### Discussion

This method is used to display a panel when JavaScript code calls `alert`. Delegates should visually indicate that this panel comes from JavaScript. The panel should have, for example, a single OK button. No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `message`: The message to display in the alert panel.

## See Also

### Opening Panels
- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](./webview%28_,runjavascriptalertpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript alert panel containing the specified message.
- [- webView:runJavaScriptConfirmPanelWithMessage:](./webview_runjavascriptconfirmpanelwithmessage_.md)
  Displays a JavaScript confirm panel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview:runjavascriptalertpanelwithmessage:)*