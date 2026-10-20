# uiDelegate

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s user interface delegate.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
unowned(unsafe) var uiDelegate: (any WebUIDelegate)! { get set }
```

```objc
@property (nonatomic, assign) id<WebUIDelegate> UIDelegate;
```

#### Discussion

A user interface delegate that conforms to the WebUIDelegate protocol.

## See Also

### Getting and Setting Delegates
- [var downloadDelegate: (any WebDownloadDelegate)!](./downloaddelegate.md)
  The receiver’s download delegate.
- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](./frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var policyDelegate: (any WebPolicyDelegate)!](./policydelegate.md)
  The receiver’s policy delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](./resourceloaddelegate.md)
  The receiver’s resource load delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/uidelegate)*