# resourceLoadDelegate

**Framework**: Webkit  
**Kind**: property

The receiver’s resource load delegate.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
unowned(unsafe) var resourceLoadDelegate: (any WebResourceLoadDelegate)! { get set }
```

#### Discussion

Conforms to the WebResourceLoadDelegate protocol.

## See Also

- [var downloadDelegate: (any WebDownloadDelegate)!](webview/downloaddelegate.md)
  The receiver’s download delegate.
- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](webview/frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var policyDelegate: (any WebPolicyDelegate)!](webview/policydelegate.md)
  The receiver’s policy delegate.
- [var uiDelegate: (any WebUIDelegate)!](webview/uidelegate.md)
  The receiver’s user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/resourceloaddelegate)*