# policyDelegate

**Framework**: WebKit  
**Kind**: property

The receiver’s policy delegate.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
unowned(unsafe) var policyDelegate: (any WebPolicyDelegate)! { get set }
```

#### Discussion

Conforms to the WebPolicyDelegate protocol.

## See Also

- [var downloadDelegate: (any WebDownloadDelegate)!](webview-swift.class/downloaddelegate.md)
  The receiver’s download delegate.
- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](webview-swift.class/frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](webview-swift.class/resourceloaddelegate.md)
  The receiver’s resource load delegate.
- [var uiDelegate: (any WebUIDelegate)!](webview-swift.class/uidelegate.md)
  The receiver’s user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/policydelegate)*