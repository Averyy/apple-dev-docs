# WKDialogResult

**Framework**: Webkit  
**Kind**: enum

An enumeration that lists the possible ways a delegate handled displaying a custom Lockdown Mode first use dialog.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
enum WKDialogResult
```

## Topics

### First use dialog results
- [WKDialogResult.askAgain](wkdialogresult/askagain.md)
  A result that indicates the delegate didn’t display a message, so other web views should check again.
- [WKDialogResult.handled](wkdialogresult/handled.md)
  A result that indicates the delegate displayed the first use message.
- [WKDialogResult.showDefault](wkdialogresult/showdefault.md)
  A result that indicates the delegate didn’t display a message, so the web view should show the default Lockdown Mode message.
### Initializers
- [init?(rawValue: Int)](wkdialogresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func webView(WKWebView, runJavaScriptAlertPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: () -> Void)](wkuidelegate/webview(_:runjavascriptalertpanelwithmessage:initiatedbyframe:completionhandler:).md)
  Displays a JavaScript alert panel.
- [func webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](wkuidelegate/webview(_:runjavascriptconfirmpanelwithmessage:initiatedbyframe:completionhandler:).md)
  Displays a JavaScript confirm panel.
- [func webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler: (String?) -> Void)](wkuidelegate/webview(_:runjavascripttextinputpanelwithprompt:defaulttext:initiatedbyframe:completionhandler:).md)
  Displays a JavaScript text input panel.
- [func webView(WKWebView, showLockdownModeFirstUseMessage: String, completionHandler: (WKDialogResult) -> Void)](wkuidelegate/webview(_:showlockdownmodefirstusemessage:completionhandler:).md)
  Displays a custom Lockdown Mode first use message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdialogresult)*