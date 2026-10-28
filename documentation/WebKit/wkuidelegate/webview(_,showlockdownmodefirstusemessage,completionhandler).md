# webView(_:showLockdownModeFirstUseMessage:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays a custom Lockdown Mode first use message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, showLockdownModeFirstUseMessage message: String, completionHandler: @escaping @MainActor @Sendable (WKDialogResult) -> Void)
```

```swift
optional func webView(_ webView: WKWebView, showLockdownModeFirstUseMessage message: String) async -> WKDialogResult
```

```objc
- (void) webView:(WKWebView *) webView showLockdownModeFirstUseMessage:(NSString *) message completionHandler:(void (^)(enum WKDialogResult)) completionHandler;
```

## Discussion

Implement this method to display a custom Lockdown Mode message, or to suppress the message. Return, or call the completion handler, with a [`WKDialogResult`](../wkdialogresult.md) case that indicates how your method handled the display request. For more information about Lockdown Mode, see [About Lockdown Mode](https://support.apple.com/en-us/HT212650).

If you don’t implement this method, the web view displays the default message.

## Parameters

- `webView`: The web view that is requesting to display the Lockdown Mode first use dialog.
- `message`: The message for the web view to display if the delegate does not display the first use dialog.
- `completionHandler`: A block you must invoke to resume after the web view displays the first use dialog. The block does not return a value, and accepts the following parameter:

  - **dialogResult**: A display result case that indicates how the method handled the display request.

## See Also

### Displaying UI panels
- [func webView(WKWebView, runJavaScriptAlertPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: () -> Void)](./webview%28_,runjavascriptalertpanelwithmessage,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript alert panel.
- [func webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](./webview%28_,runjavascriptconfirmpanelwithmessage,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript confirm panel.
- [func webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler: (String?) -> Void)](./webview%28_,runjavascripttextinputpanelwithprompt,defaulttext,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript text input panel.
- [enum WKDialogResult](../wkdialogresult.md)
  An enumeration that lists the possible ways a delegate handled displaying a custom Lockdown Mode first use dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:showlockdownmodefirstusemessage:completionhandler:))*