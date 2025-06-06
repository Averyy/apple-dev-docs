# frameLoadDelegate

**Framework**: Webkit  
**Kind**: property

The receiver’s frame load delegate.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
unowned(unsafe) var frameLoadDelegate: (any WebFrameLoadDelegate)! { get set }
```

#### Discussion

Conforms to the WebFrameLoadDelegate protocol.

## See Also

- [var downloadDelegate: (any WebDownloadDelegate)!](webview/downloaddelegate.md)
  The receiver’s download delegate.
- [var policyDelegate: (any WebPolicyDelegate)!](webview/policydelegate.md)
  The receiver’s policy delegate.
- [var resourceLoadDelegate: (any WebResourceLoadDelegate)!](webview/resourceloaddelegate.md)
  The receiver’s resource load delegate.
- [var uiDelegate: (any WebUIDelegate)!](webview/uidelegate.md)
  The receiver’s user interface delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/frameloaddelegate)*