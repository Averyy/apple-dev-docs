# webView(_:showLockdownModeFirstUseMessage:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Displays a custom Lockdown Mode first use message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func webView(_ webView: WKWebView, showLockdownModeFirstUseMessage message: String) async -> WKDialogResult
```

#### Discussion

Implement this method to display a custom Lockdown Mode message, or to suppress the message. Return, or call the completion handler, with a [`WKDialogResult`](wkdialogresult.md) case that indicates how your method handled the display request. For more information about Lockdown Mode, see [`About Lockdown Mode`](https://developer.apple.comhttps://support.apple.com/en-us/HT212650).

If you don’t implement this method, the web view displays the default message.

## Parameters

- `webView`: The web view that is requesting to display the Lockdown Mode first use dialog.
- `message`: The message for the web view to display if the delegate does not display the first use dialog.
- `completionHandler`: A block you must invoke to resume after the web view displays the first use dialog. The block does not return a value, and accepts the following parameter:

## See Also

- [func webView(WKWebView, runJavaScriptAlertPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: () -> Void)](wkuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedbyframe:completionhandler:).md)
  Displays a JavaScript alert panel.
- [func webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](wkuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedbyframe:completionhandler:).md)
  Displays a JavaScript confirm panel.
- [func webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler: (String?) -> Void)](wkuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedbyframe:completionhandler:).md)
  Displays a JavaScript text input panel.
- [enum WKDialogResult](wkdialogresult.md)
  An enumeration that lists the possible ways a delegate handled displaying a custom Lockdown Mode first use dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:showlockdownmodefirstusemessage:completionhandler:))*