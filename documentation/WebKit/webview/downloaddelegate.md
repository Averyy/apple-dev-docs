# downloadDelegate

**Framework**: Webkit  
**Kind**: property

The receiver’s download delegate.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
unowned(unsafe) var downloadDelegate: (any WebDownloadDelegate)! { get set }
```

#### Discussion

Implements the [`WebDownload`](webdownload.md) protocol.

WebKit may create `WebDownload` objects automatically to handle downloads that start with a webpage or link.

## See Also

- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](webview/frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var policyDelegate: (any WebPolicyDelegate)!](webview/policydelegate.md)
  The receiver’s policy delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](webview/resourceloaddelegate.md)
  The receiver’s resource load delegate.
- [var uiDelegate: (any WebUIDelegate)!](webview/uidelegate.md)
  The receiver’s user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/downloaddelegate)*