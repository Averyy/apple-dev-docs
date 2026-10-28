# webView(_:runOpenPanelForFileButtonWith:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays an open panel for a file input control.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, runOpenPanelForFileButtonWith resultListener: (any WebOpenPanelResultListener)!)
```

```objc
- (void) webView:(WebView *) sender runOpenPanelForFileButtonWithResultListener:(id<WebOpenPanelResultListener>) resultListener;
```

## Discussion

This method uses a listener object to set the results of the open panel, instead of returning the value directly. This approach allows delegates to implement the open panel as a modal dialog. No action is taken if you do not implement this method.

## Parameters

- `sender`: The web view that sent the message.
- `resultListener`: See the [`WebOpenPanelResultListener`](../webopenpanelresultlistener.md) protocol for how to set these values.

## See Also

### Opening Panels
- [func webView(WebView!, runJavaScriptAlertPanelWithMessage: String!, initiatedBy: WebFrame!)](./webview%28_,runjavascriptalertpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript alert panel containing the specified message.
- [func webView(WebView!, runJavaScriptConfirmPanelWithMessage: String!, initiatedBy: WebFrame!) -> Bool](./webview%28_,runjavascriptconfirmpanelwithmessage,initiatedby%29.md)
  Displays a JavaScript confirmation panel with the specified message.
- [func webView(WebView!, runJavaScriptTextInputPanelWithPrompt: String!, defaultText: String!, initiatedBy: WebFrame!) -> String!](./webview%28_,runjavascripttextinputpanelwithprompt,defaulttext,initiatedby%29.md)
  Displays a JavaScript text input panel and returns the entered text.
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](./webview%28_,runopenpanelforfilebuttonwith,allowmultiplefiles%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runopenpanelforfilebuttonwith:))*