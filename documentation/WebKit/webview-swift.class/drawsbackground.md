# drawsBackground

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the web view draws a background.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property (nonatomic) BOOL drawsBackground;
```

## Discussion

If [`true`](../../Swift/true.md), a default background is drawn; if [`false`](../../Swift/false.md), it is not.

## See Also

### Drawing
- [var shouldUpdateWhileOffscreen: Bool](./shouldupdatewhileoffscreen.md)
  A Boolean that inidicates whether the web view should update even when it is not in a window that is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/drawsbackground)*