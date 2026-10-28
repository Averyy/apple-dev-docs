# WebViewProgressEstimateChangedNotification

**Framework**: WebKit  
**Kind**: var  
**Role**: Global Variable

Posted by a WebView object when the estimated progress value of a load changes.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```c
extern NSString * WebViewProgressEstimateChangedNotification;
```

## Discussion

This notification may be posted zero or more times after a [`WebViewProgressStartedNotification`](./webviewprogressstartednotification.md) notification is posted. The notification object is the WebView for which the progress value has changed. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation
- [var estimatedProgress: Double](./webview-swift.class/estimatedprogress.md)
  An estimate, as a percentage, of the amount of content that is currently loaded.
### Notifications
- [WebViewDidBeginEditingNotification](./webviewdidbegineditingnotification.md)
  Posted when a web view begins any operation that changes its contents in response to user editing.
- [WebViewDidChangeNotification](./webviewdidchangenotification.md)
  Posted when a web view performs any operation that changes its contents in response to user editing.
- [WebViewDidChangeSelectionNotification](./webviewdidchangeselectionnotification.md)
  Posted when a web view changes its typing selection.
- [WebViewDidChangeTypingStyleNotification](./webviewdidchangetypingstylenotification.md)
  Posted when a web view changes its typing style.
- [WebViewDidEndEditingNotification](./webviewdidendeditingnotification.md)
  Posted when a web view ends any operation that changes its contents in response to user editing.
- [WebViewProgressFinishedNotification](./webviewprogressfinishednotification.md)
  Posted by a WebView object when the load has finished.
- [WebViewProgressStartedNotification](./webviewprogressstartednotification.md)
  Posted by a WebView object when a load begins, including a load that is initiated in a subframe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webviewprogressestimatechangednotification)*