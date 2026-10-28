# WKError.Code.contentRuleListStoreLookUpFailed

**Framework**: WebKit  
**Kind**: case  
**Role**: Case

An error that indicates a content rule list data store didn’t find a rule list with the specified identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
case contentRuleListStoreLookUpFailed
```

```c
WKErrorContentRuleListStoreLookUpFailed
```

## Discussion

This error might occur if you previously deleted the rule list.

## See Also

### Errors
- [WKError.Code.unknown](./unknown.md)
  An error that indicates an unknown issue occurred.
- [WKError.Code.webContentProcessTerminated](./webcontentprocessterminated.md)
  An error that indicates the web process that contains the content is no longer running.
- [WKError.Code.webViewInvalidated](./webviewinvalidated.md)
  An error that indicates the web view was invalidated.
- [WKError.Code.javaScriptExceptionOccurred](./javascriptexceptionoccurred.md)
  An error that indicates a JavaScript exception occurred.
- [WKError.Code.javaScriptResultTypeIsUnsupported](./javascriptresulttypeisunsupported.md)
  An error that indicates the result of JavaScript execution could not be returned.
- [WKError.Code.contentRuleListStoreCompileFailed](./contentruleliststorecompilefailed.md)
  An error that indicates the compilation of a rule list failed.
- [WKError.Code.contentRuleListStoreRemoveFailed](./contentruleliststoreremovefailed.md)
  An error that indicates a failure to remove a content rule list from the rule list data store object.
- [WKError.Code.contentRuleListStoreVersionMismatch](./contentruleliststoreversionmismatch.md)
  An error that indicates the rule list version is outdated and cannot be read.
- [WKError.Code.attributedStringContentFailedToLoad](./attributedstringcontentfailedtoload.md)
  An error that indicates the failure to navigate to web content from an attributed string.
- [WKError.Code.attributedStringContentLoadTimedOut](./attributedstringcontentloadtimedout.md)
  An error that indicates a timeout occurred while trying to load web content from an attributed string.
- [WKError.Code.javaScriptInvalidFrameTarget](./javascriptinvalidframetarget.md)
  An error that indicates your content referenced an invalid web frame.
- [WKError.Code.navigationAppBoundDomain](./navigationappbounddomain.md)
  An error that indicates navigation failed due to an app-bound domain restriction.
- [WKError.Code.javaScriptAppBoundDomain](./javascriptappbounddomain.md)
  An error that indicates JavaScript execution failed due to an app-bound domain restriction.
- [WKError.Code.credentialNotFound](./credentialnotfound.md)
  An error that indicates the system could not find a passkey during an export.
- [WKError.Code.duplicateCredential](./duplicatecredential.md)
  An error that indicates the system found a duplicate passkey during an import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkerror/code/contentruleliststorelookupfailed)*