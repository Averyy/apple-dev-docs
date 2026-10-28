# webView(_:runBeforeUnloadConfirmPanelWithMessage:initiatedBy:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays a confirmation panel containing the specified message before a window closes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func webView(_ sender: WebView!, runBeforeUnloadConfirmPanelWithMessage message: String!, initiatedBy frame: WebFrame!) -> Bool
```

```objc
- (BOOL) webView:(WebView *) sender runBeforeUnloadConfirmPanelWithMessage:(NSString *) message initiatedByFrame:(WebFrame *) frame;
```

## Return Value

[`true`](../../Swift/true.md) if the user clicked the OK button; otherwise, [`false`](../../Swift/false.md).

## Discussion

Use this method to include a message in the confirmation panel in addition to the message supplied by the webpage. The confirmation panel should contain OK and Cancel buttons.

## Parameters

- `sender`: The web view that sent the message.
- `message`: The message to display in the panel.
- `frame`: The web frame whose JavaScript initiated this call.

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
- [func webView(WebView!, runOpenPanelForFileButtonWith: (any WebOpenPanelResultListener)!, allowMultipleFiles: Bool)](./webview%28_,runopenpanelforfilebuttonwith,allowmultiplefiles%29.md)
  Displays an open panel for a file input control.
- [- webView:runJavaScriptAlertPanelWithMessage:](./webview_runjavascriptalertpanelwithmessage_.md)
  Displays a JavaScript alert panel.
- [- webView:runJavaScriptConfirmPanelWithMessage:](./webview_runjavascriptconfirmpanelwithmessage_.md)
  Displays a JavaScript confirm panel.
- [- webView:runJavaScriptTextInputPanelWithPrompt:defaultText:](./webview_runjavascripttextinputpanelwithprompt_defaulttext_.md)
  Displays a JavaScript text input panel and returns the entered text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webuidelegate/webview(_:runbeforeunloadconfirmpanelwithmessage:initiatedby:))*