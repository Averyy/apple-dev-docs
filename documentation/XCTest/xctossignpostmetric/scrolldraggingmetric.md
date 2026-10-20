# scrollDraggingMetric

**Framework**: XCTest  
**Kind**: property  
**Role**: Type Property

A metric that records scroll-dragging animations.

**Availability**:
- xcode 12.0+ - Deprecated in 13.0

> **Deprecated**: Use [`scrollingAndDecelerationMetric`](./scrollinganddecelerationmetric.md) instead.

## Declaration

```swift
class var scrollDraggingMetric: any XCTMetric { get }
```

```objc
@property (class, readonly) id<XCTMetric> scrollDraggingMetric;
```

## See Also

### Deprecated
- [class var applicationLaunch: XCTOSSignpostMetric](./applicationlaunch.md)
  A metric that records the time that elapses during app launch.
- [class var scrollDecelerationMetric: any XCTMetric](./scrolldecelerationmetric.md)
  A metric that records scroll deceleration animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric/scrolldraggingmetric)*