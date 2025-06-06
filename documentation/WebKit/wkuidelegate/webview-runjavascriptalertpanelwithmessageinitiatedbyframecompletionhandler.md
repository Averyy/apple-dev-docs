# webView(_:runJavaScriptAlertPanelWithMessage:initiatedByFrame:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Displays a JavaScript alert panel.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo) async
```

#### Discussion

For user security, implementations of this method should call attention to the fact that a specific website controls the content in this panel. A simple formula for identifying the controlling website is `frame.request.URL.host`. The panel should have a single OK button.

## Parameters

- `webView`: The web view invoking the delegate method.
- `message`: The message to be displayed.
- `frame`: Information about the frame whose JavaScript process initiated this call.
- `completionHandler`: The completion handler to call after the alert panel has been dismissed.

## See Also

- [func webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](wkuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedbyframe:completionhandler:).md)
  Displays a JavaScript confirm panel.
- [func webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler: (String?) -> Void)](wkuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedbyframe:completionhandler:).md)
  Displays a JavaScript text input panel.
- [func webView(WKWebView, showLockdownModeFirstUseMessage: String, completionHandler: (WKDialogResult) -> Void)](wkuidelegate/webview(_:showlockdownmodefirstusemessage:completionhandler:).md)
  Displays a custom Lockdown Mode first use message.
- [enum WKDialogResult](wkdialogresult.md)
  An enumeration that lists the possible ways a delegate handled displaying a custom Lockdown Mode first use dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedbyframe:completionhandler:))*