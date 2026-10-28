# wantsSoftwareDimming

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the screen may be dimmed lower than the hardware is normally capable of by emulating it in software.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var wantsSoftwareDimming: Bool { get set }
```

```objc
@property (nonatomic) BOOL wantsSoftwareDimming;
```

## Discussion

The default value is [`false`](../../Swift/false.md). Enabling it may cause a loss in performance.

## See Also

### Managing brightness
- [var brightness: CGFloat](./brightness.md)
  The brightness level of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/wantssoftwaredimming)*