# shouldUpdateWhileOffscreen

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that inidicates whether the web view should update even when it is not in a window that is currently visible.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var shouldUpdateWhileOffscreen: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldUpdateWhileOffscreen;
```

## Discussion

If [`true`](../../Swift/true.md), the web view updates regardless if it is visible. If [`false`](../../Swift/false.md), it updates only if it is visible, possibly improving performance, and then updates automatically when it becomes visible. The default value is [`true`](../../Swift/true.md).

## See Also

### Drawing
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean that indicates whether the web view draws a background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/shouldupdatewhileoffscreen)*