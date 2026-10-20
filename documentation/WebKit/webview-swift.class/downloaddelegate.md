# downloadDelegate

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s download delegate.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
unowned(unsafe) var downloadDelegate: (any WebDownloadDelegate)! { get set }
```

```objc
@property (nonatomic, assign) id<WebDownloadDelegate> downloadDelegate;
```

#### Discussion

Implements the [`WebDownload`](../webdownload.md) protocol.

WebKit may create `WebDownload` objects automatically to handle downloads that start with a webpage or link.

## See Also

### Getting and Setting Delegates
- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](./frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var policyDelegate: (any WebPolicyDelegate)!](./policydelegate.md)
  The receiver’s policy delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](./resourceloaddelegate.md)
  The receiver’s resource load delegate.
- [var uiDelegate: (any WebUIDelegate)!](./uidelegate.md)
  The receiver’s user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/downloaddelegate)*