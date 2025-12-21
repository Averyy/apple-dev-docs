# wantsSoftwareDimming

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the screen may be dimmed lower than the hardware is normally capable of by emulating it in software.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var wantsSoftwareDimming: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). Enabling it may cause a loss in performance.

## See Also

- [var brightness: CGFloat](uiscreen/brightness.md)
  The brightness level of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/wantssoftwaredimming)*