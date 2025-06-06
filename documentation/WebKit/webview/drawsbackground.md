# drawsBackground

**Framework**: Webkit  
**Kind**: property

A Boolean that indicates whether the web view draws a background.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), a default background is drawn; if [`false`](https://developer.apple.com/documentation/swift/false), it is not.

## See Also

- [var shouldUpdateWhileOffscreen: Bool](webview/shouldupdatewhileoffscreen.md)
  A Boolean that inidicates whether the web view should update even when it is not in a window that is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/drawsbackground)*