# webView(_:runJavaScriptAlertPanelWithMessage:initiatedByFrame:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Displays a JavaScript alert panel.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping @MainActor @Sendable () -> Void)
```

```swift
optional func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo) async
```

```objc
- (void) webView:(WKWebView *) webView runJavaScriptAlertPanelWithMessage:(NSString *) message initiatedByFrame:(WKFrameInfo *) frame completionHandler:(void (^)(void)) completionHandler;
```

## Discussion

For user security, implementations of this method should call attention to the fact that a specific website controls the content in this panel. A simple formula for identifying the controlling website is `frame.request.URL.host`. The panel should have a single OK button.

## Parameters

- `webView`: The web view invoking the delegate method.
- `message`: The message to be displayed.
- `frame`: Information about the frame whose JavaScript process initiated this call.
- `completionHandler`: The completion handler to call after the alert panel has been dismissed.

## See Also

### Displaying UI panels
- [func webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](./webview%28_,runjavascriptconfirmpanelwithmessage,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript confirm panel.
- [func webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler: (String?) -> Void)](./webview%28_,runjavascripttextinputpanelwithprompt,defaulttext,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript text input panel.
- [func webView(WKWebView, showLockdownModeFirstUseMessage: String, completionHandler: (WKDialogResult) -> Void)](./webview%28_,showlockdownmodefirstusemessage,completionhandler%29.md)
  Displays a custom Lockdown Mode first use message.
- [enum WKDialogResult](../wkdialogresult.md)
  An enumeration that lists the possible ways a delegate handled displaying a custom Lockdown Mode first use dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedbyframe:completionhandler:))*