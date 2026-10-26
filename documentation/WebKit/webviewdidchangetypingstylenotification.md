# WebViewDidChangeTypingStyleNotification

**Framework**: WebKit  
**Kind**: var  
**Role**: Global Variable

Posted when a web view changes its typing style.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```c
extern NSString * const WebViewDidChangeTypingStyleNotification;
```

#### Discussion

The notification object is the WebView that changed its typing style. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation
- [var typingStyle: DOMCSSStyleDeclaration!](./webview-swift.class/typingstyle.md)
  The receiver’s CSS typing style.
### Notifications
- [WebViewDidBeginEditingNotification](./webviewdidbegineditingnotification.md)
  Posted when a web view begins any operation that changes its contents in response to user editing.
- [WebViewDidChangeNotification](./webviewdidchangenotification.md)
  Posted when a web view performs any operation that changes its contents in response to user editing.
- [WebViewDidChangeSelectionNotification](./webviewdidchangeselectionnotification.md)
  Posted when a web view changes its typing selection.
- [WebViewDidEndEditingNotification](./webviewdidendeditingnotification.md)
  Posted when a web view ends any operation that changes its contents in response to user editing.
- [WebViewProgressEstimateChangedNotification](./webviewprogressestimatechangednotification.md)
  Posted by a WebView object when the estimated progress value of a load changes.
- [WebViewProgressFinishedNotification](./webviewprogressfinishednotification.md)
  Posted by a WebView object when the load has finished.
- [WebViewProgressStartedNotification](./webviewprogressstartednotification.md)
  Posted by a WebView object when a load begins, including a load that is initiated in a subframe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webviewdidchangetypingstylenotification)*