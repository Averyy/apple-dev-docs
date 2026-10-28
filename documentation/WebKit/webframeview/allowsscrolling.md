# allowsScrolling

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the frame view should allow users to scroll.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var allowsScrolling: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsScrolling;
```

## Discussion

If [`true`](../../Swift/true.md), scrolling is allowed; if [`false`](../../Swift/false.md), it is not. If the frame contains a scrolling element, then that value is used as the default; otherwise, the default is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/allowsscrolling)*