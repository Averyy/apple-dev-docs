# scrollDecelerationMetric

**Framework**: XCTest  
**Kind**: property  
**Role**: Type Property

A metric that records scroll deceleration animations.

**Availability**:
- xcode 12.0+ - Deprecated in 13.0

> **Deprecated**: Use [`scrollingAndDecelerationMetric`](./scrollinganddecelerationmetric.md) instead.

## Declaration

```swift
class var scrollDecelerationMetric: any XCTMetric { get }
```

```objc
@property (class, readonly) id<XCTMetric> scrollDecelerationMetric;
```

## See Also

### Deprecated
- [class var applicationLaunch: XCTOSSignpostMetric](./applicationlaunch.md)
  A metric that records the time that elapses during app launch.
- [class var scrollDraggingMetric: any XCTMetric](./scrolldraggingmetric.md)
  A metric that records scroll-dragging animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric/scrolldecelerationmetric)*