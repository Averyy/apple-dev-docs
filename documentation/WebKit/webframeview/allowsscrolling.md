# allowsScrolling

**Framework**: Webkit  
**Kind**: property

A Boolean that indicates whether the frame view should allow users to scroll.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var allowsScrolling: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), scrolling is allowed; if [`false`](https://developer.apple.com/documentation/swift/false), it is not. If the frame contains a scrolling element, then that value is used as the default; otherwise, the default is [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/allowsscrolling)*