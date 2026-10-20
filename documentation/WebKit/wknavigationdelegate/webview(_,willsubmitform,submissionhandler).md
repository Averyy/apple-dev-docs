# webView(_:willSubmitForm:submissionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func webView(_ webView: WKWebView, willSubmitForm formInfo: WKFormInfo, submissionHandler: @escaping @MainActor @Sendable () -> Void)
```

```swift
optional func webView(_ webView: WKWebView, willSubmitForm formInfo: WKFormInfo) async
```

```objc
- (void) webView:(WKWebView *) webView willSubmitForm:(WKFormInfo *) formInfo submissionHandler:(void (^)(void)) submissionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationdelegate/webview(_:willsubmitform:submissionhandler:))*