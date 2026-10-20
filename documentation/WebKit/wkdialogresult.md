# WKDialogResult

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that lists the possible ways a delegate handled displaying a custom Lockdown Mode first use dialog.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
enum WKDialogResult
```

```c
enum WKDialogResult : NSInteger;
```

## Topics

### First use dialog results
- [WKDialogResult.askAgain](./wkdialogresult/askagain.md)
  A result that indicates the delegate didn’t display a message, so other web views should check again.
- [WKDialogResult.handled](./wkdialogresult/handled.md)
  A result that indicates the delegate displayed the first use message.
- [WKDialogResult.showDefault](./wkdialogresult/showdefault.md)
  A result that indicates the delegate didn’t display a message, so the web view should show the default Lockdown Mode message.
### Initializers
- [init?(rawValue: Int)](./wkdialogresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Displaying UI panels
- [func webView(WKWebView, runJavaScriptAlertPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: () -> Void)](./wkuidelegate/webview%28_,runjavascriptalertpanelwithmessage,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript alert panel.
- [func webView(WKWebView, runJavaScriptConfirmPanelWithMessage: String, initiatedByFrame: WKFrameInfo, completionHandler: (Bool) -> Void)](./wkuidelegate/webview%28_,runjavascriptconfirmpanelwithmessage,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript confirm panel.
- [func webView(WKWebView, runJavaScriptTextInputPanelWithPrompt: String, defaultText: String?, initiatedByFrame: WKFrameInfo, completionHandler: (String?) -> Void)](./wkuidelegate/webview%28_,runjavascripttextinputpanelwithprompt,defaulttext,initiatedbyframe,completionhandler%29.md)
  Displays a JavaScript text input panel.
- [func webView(WKWebView, showLockdownModeFirstUseMessage: String, completionHandler: (WKDialogResult) -> Void)](./wkuidelegate/webview%28_,showlockdownmodefirstusemessage,completionhandler%29.md)
  Displays a custom Lockdown Mode first use message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdialogresult)*