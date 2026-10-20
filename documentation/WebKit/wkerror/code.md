# WKError.Code

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

Possible error values that WebKit APIs can return.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum WKErrorCode : NSInteger;
```

## Topics

### Errors
- [WKError.Code.unknown](./code/unknown.md)
  An error that indicates an unknown issue occurred.
- [WKError.Code.webContentProcessTerminated](./code/webcontentprocessterminated.md)
  An error that indicates the web process that contains the content is no longer running.
- [WKError.Code.webViewInvalidated](./code/webviewinvalidated.md)
  An error that indicates the web view was invalidated.
- [WKError.Code.javaScriptExceptionOccurred](./code/javascriptexceptionoccurred.md)
  An error that indicates a JavaScript exception occurred.
- [WKError.Code.javaScriptResultTypeIsUnsupported](./code/javascriptresulttypeisunsupported.md)
  An error that indicates the result of JavaScript execution could not be returned.
- [WKError.Code.contentRuleListStoreCompileFailed](./code/contentruleliststorecompilefailed.md)
  An error that indicates the compilation of a rule list failed.
- [WKError.Code.contentRuleListStoreLookUpFailed](./code/contentruleliststorelookupfailed.md)
  An error that indicates a content rule list data store didn’t find a rule list with the specified identifier.
- [WKError.Code.contentRuleListStoreRemoveFailed](./code/contentruleliststoreremovefailed.md)
  An error that indicates a failure to remove a content rule list from the rule list data store object.
- [WKError.Code.contentRuleListStoreVersionMismatch](./code/contentruleliststoreversionmismatch.md)
  An error that indicates the rule list version is outdated and cannot be read.
- [WKError.Code.attributedStringContentFailedToLoad](./code/attributedstringcontentfailedtoload.md)
  An error that indicates the failure to navigate to web content from an attributed string.
- [WKError.Code.attributedStringContentLoadTimedOut](./code/attributedstringcontentloadtimedout.md)
  An error that indicates a timeout occurred while trying to load web content from an attributed string.
- [WKError.Code.javaScriptInvalidFrameTarget](./code/javascriptinvalidframetarget.md)
  An error that indicates your content referenced an invalid web frame.
- [WKError.Code.navigationAppBoundDomain](./code/navigationappbounddomain.md)
  An error that indicates navigation failed due to an app-bound domain restriction.
- [WKError.Code.javaScriptAppBoundDomain](./code/javascriptappbounddomain.md)
  An error that indicates JavaScript execution failed due to an app-bound domain restriction.
- [WKError.Code.credentialNotFound](./code/credentialnotfound.md)
  An error that indicates the system could not find a passkey during an export.
- [WKError.Code.duplicateCredential](./code/duplicatecredential.md)
  An error that indicates the system found a duplicate passkey during an import.
- [WKError.Code.malformedCredential](./code/malformedcredential.md)
  An error that indicates the system could not parse passkey data during an import.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct WKError](../wkerror.md)
  Possible error values that WebKit APIs can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkerror/code)*