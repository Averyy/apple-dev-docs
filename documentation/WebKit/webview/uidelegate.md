# uiDelegate

**Framework**: Webkit  
**Kind**: property

The receiver’s user interface delegate.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
unowned(unsafe) var uiDelegate: (any WebUIDelegate)! { get set }
```

#### Discussion

A user interface delegate that conforms to the WebUIDelegate protocol.

## See Also

- [var downloadDelegate: (any WebDownloadDelegate)!](webview/downloaddelegate.md)
  The receiver’s download delegate.
- [var frameLoadDelegate: (any WebFrameLoadDelegate)!](webview/frameloaddelegate.md)
  The receiver’s frame load delegate.
- [var policyDelegate: (any WebPolicyDelegate)!](webview/policydelegate.md)
  The receiver’s policy delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](webview/resourceloaddelegate.md)
  The receiver’s resource load delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/uidelegate)*