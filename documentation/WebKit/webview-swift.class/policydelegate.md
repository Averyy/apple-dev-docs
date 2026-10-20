# policyDelegate

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s policy delegate.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
unowned(unsafe) var policyDelegate: (any WebPolicyDelegate)! { get set }
```

```objc
@property (nonatomic, assign) id<WebPolicyDelegate> policyDelegate;
```

#### Discussion

Conforms to the WebPolicyDelegate protocol.

## See Also

### Getting and Setting Delegates
- [var downloadDelegate: (any WebDownloadDelegate)!](./downloaddelegate.md)
  The receiver’s download delegate.
- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](./frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](./resourceloaddelegate.md)
  The receiver’s resource load delegate.
- [var uiDelegate: (any WebUIDelegate)!](./uidelegate.md)
  The receiver’s user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/policydelegate)*