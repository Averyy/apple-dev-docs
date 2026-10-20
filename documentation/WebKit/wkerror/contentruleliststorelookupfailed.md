# contentRuleListStoreLookUpFailed

**Framework**: WebKit  
**Kind**: property  
**Role**: Type Property

An error that indicates a content rule list data store didn’t find a rule list with the specified identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
static var contentRuleListStoreLookUpFailed: WKError.Code { get }
```

#### Discussion

This error might occur if you previously deleted the rule list.

## See Also

### Getting the Error Codes
- [static var unknown: WKError.Code](./unknown.md)
  An error that indicates an unknown issue occurred.
- [static var webContentProcessTerminated: WKError.Code](./webcontentprocessterminated.md)
  An error that indicates the web process that contains the content is no longer running.
- [static var webViewInvalidated: WKError.Code](./webviewinvalidated.md)
  An error that indicates the web view was invalidated.
- [static var javaScriptExceptionOccurred: WKError.Code](./javascriptexceptionoccurred.md)
  An error that indicates a JavaScript exception occurred.
- [static var javaScriptResultTypeIsUnsupported: WKError.Code](./javascriptresulttypeisunsupported.md)
  An error that indicates the result of JavaScript execution could not be returned.
- [static var contentRuleListStoreCompileFailed: WKError.Code](./contentruleliststorecompilefailed.md)
  An error that indicates the compilation of a rule list failed.
- [static var contentRuleListStoreRemoveFailed: WKError.Code](./contentruleliststoreremovefailed.md)
  An error that indicates a failure to remove a content rule list from the rule list data store object.
- [static var contentRuleListStoreVersionMismatch: WKError.Code](./contentruleliststoreversionmismatch.md)
  An error that indicates the rule list version is outdated and cannot be read.
- [static var attributedStringContentFailedToLoad: WKError.Code](./attributedstringcontentfailedtoload.md)
  An error that indicates the failure to navigate to web content from an attributed string.
- [static var attributedStringContentLoadTimedOut: WKError.Code](./attributedstringcontentloadtimedout.md)
  An error that indicates a timeout occurred while trying to load web content from an attributed string.
- [static var javaScriptInvalidFrameTarget: WKError.Code](./javascriptinvalidframetarget.md)
  An error that indicates your content referenced an invalid web frame.
- [static var navigationAppBoundDomain: WKError.Code](./navigationappbounddomain.md)
  An error that indicates navigation failed due to an app-bound domain restriction.
- [static var javaScriptAppBoundDomain: WKError.Code](./javascriptappbounddomain.md)
  An error that indicates JavaScript execution failed due to an app-bound domain restriction.
- [static var credentialNotFound: WKError.Code](./credentialnotfound.md)
  An error that indicates the system could not find a passkey during an export.
- [static var duplicateCredential: WKError.Code](./duplicatecredential.md)
  An error that indicates the system found a duplicate passkey during an import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkerror/contentruleliststorelookupfailed)*