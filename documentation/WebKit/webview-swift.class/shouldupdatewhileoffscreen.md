# shouldUpdateWhileOffscreen

**Framework**: WebKit  
**Kind**: property

A Boolean that inidicates whether the web view should update even when it is not in a window that is currently visible.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var shouldUpdateWhileOffscreen: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the web view updates regardless if it is visible. If [`false`](https://developer.apple.com/documentation/Swift/false), it updates only if it is visible, possibly improving performance, and then updates automatically when it becomes visible. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var drawsBackground: Bool](webview-swift.class/drawsbackground.md)
  A Boolean that indicates whether the web view draws a background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/shouldupdatewhileoffscreen)*