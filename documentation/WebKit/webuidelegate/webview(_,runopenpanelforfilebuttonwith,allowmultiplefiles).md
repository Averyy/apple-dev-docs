# webView(_:runOpenPanelForFileButtonWith:allowMultipleFiles:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays an open panel for a file input control.

**Availability**:
- macOS 10.6+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, runOpenPanelForFileButtonWith resultListener: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)
```

```objc
- (void) webView:(WebView *) sender runOpenPanelForFileButtonWithResultListener:(id<WebOpenPanelResultListener>) resultListener allowMultipleFiles:(BOOL) allowMultipleFiles;
```

## Parameters

- `sender`: The web view that sent the message.
- `resultListener`: See the [`WebOpenPanelResultListener`](../webopenpanelresultlistener.md) protocol for how to set these values.
- `allowMultipleFiles`: If [`true`](../../Swift/true.md), the open panel should allow multiple files to be selected; otherwise, it should not.

## See Also

### Opening Panels
- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](./webview%28_,runjavascriptalertpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](./webview%28_,runjavascriptconfirmpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](./webview%28_,runjavascripttextinputpanelwithprompt,defaulttext,initiatedby%29.md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!)](./webview%28_,runopenpanelforfilebuttonwith%29.md)
  Displays an open panel for a file input control.
- [func webView(WebView!, runBeforeUnloadConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](./webview%28_,runbeforeunloadconfirmpanelwithmessage,initiatedby%29.md)
  Displays a confirmation panel containing the specified message before a window closes.
- [- webView:runJavaScriptAlertPanelWithMessage:](./webview_runjavascriptalertpanelwithmessage_.md)
  Displays a JavaScript alert panel.
- [- webView:runJavaScriptConfirmPanelWithMessage:](./webview_runjavascriptconfirmpanelwithmessage_.md)
  Displays a JavaScript confirm panel.
- [- webView:runJavaScriptTextInputPanelWithPrompt:defaultText:](./webview_runjavascripttextinputpanelwithprompt_defaulttext_.md)
  Displays a JavaScript text input panel and returns the entered text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runopenpanelforfilebuttonwith:allowmultiplefiles:))*