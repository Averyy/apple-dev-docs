# applicationLaunch

**Framework**: XCTest  
**Kind**: property  
**Role**: Type Property

A metric that records the time that elapses during app launch.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0
- Mac Catalyst 13.0+ - Deprecated in 14.0
- macOS 10.15+ - Deprecated in 11.0
- tvOS 13.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`XCTApplicationLaunchMetric`](../xctapplicationlaunchmetric.md) instead.

## Declaration

```swift
class var applicationLaunch: XCTOSSignpostMetric { get }
```

```objc
@property (class, readonly) XCTOSSignpostMetric * applicationLaunchMetric;
```

## See Also

### Deprecated
- [class var scrollDecelerationMetric: any XCTMetric](./scrolldecelerationmetric.md)
  A metric that records scroll deceleration animations.
- [class var scrollDraggingMetric: any XCTMetric](./scrolldraggingmetric.md)
  A metric that records scroll-dragging animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric/applicationlaunch)*