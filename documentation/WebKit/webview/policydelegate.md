# policyDelegate

**Framework**: Webkit  
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

- [var downloadDelegate: (any WebDownloadDelegate)!](webview/downloaddelegate.md)
  The receiver’s download delegate.
- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](webview/frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](webview/resourceloaddelegate.md)
  The receiver’s resource load delegate.
- [var uiDelegate: (any WebUIDelegate)!](webview/uidelegate.md)
  The receiver’s user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/policydelegate)*