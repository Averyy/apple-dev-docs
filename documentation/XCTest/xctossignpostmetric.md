# XCTOSSignpostMetric

**Framework**: Xctest  
**Kind**: class

A metric to record the time that a performance test spends executing a signposted region of code.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class XCTOSSignpostMetric
```

#### Overview

This metric captures the time that elapses between the [`begin`](https://developer.apple.com/documentation/os/OSSignpostType/begin) and [`end`](https://developer.apple.com/documentation/os/OSSignpostType/end) events for a specific named [`os_signpost(_:dso:log:name:signpostID:)`](https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostID:)-2oz8u) region. It doesn’t record any results when there isn’t a matching pair of `begin` and `end` events.

## Topics

### Measuring Specific Signposts
- [init(subsystem: String, category: String, name: String)](xctossignpostmetric/init(subsystem:category:name:).md)
  Creates a metric to record a specific signpost.
### Measuring Navigation Transitions
- [class var customNavigationTransitionMetric: any XCTMetric](xctossignpostmetric/customnavigationtransitionmetric.md)
  A metric that records the duration of custom navigation transitions between views.
- [class var navigationTransitionMetric: any XCTMetric](xctossignpostmetric/navigationtransitionmetric.md)
  A metric that records the duration of navigation transitions between views.
### Measuring Scrolling Properties
- [class var scrollingAndDecelerationMetric: any XCTMetric](xctossignpostmetric/scrollinganddecelerationmetric.md)
  A metric that records scroll-dragging and deceleration animations.
### Deprecated
- [class var applicationLaunch: XCTOSSignpostMetric](xctossignpostmetric/applicationlaunch.md)
  A metric that records the time that elapses during app launch.
- [class var scrollDecelerationMetric: any XCTMetric](xctossignpostmetric/scrolldecelerationmetric.md)
  A metric that records scroll deceleration animations.
- [class var scrollDraggingMetric: any XCTMetric](xctossignpostmetric/scrolldraggingmetric.md)
  A metric that records scroll-dragging animations.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [XCTMetric](xctmetric.md)

## See Also

- [protocol XCTMetric](xctmetric.md)
  A protocol that defines the methods that objects must provide when gathering metrics during performance tests.
- [class XCTCPUMetric](xctcpumetric.md)
  A metric to record information about CPU activity during a performance test.
- [class XCTClockMetric](xctclockmetric.md)
  A metric to record the time that elapses during a performance test.
- [class XCTMemoryMetric](xctmemorymetric.md)
  A metric to record the physical memory that a performance test uses.
- [class XCTStorageMetric](xctstoragemetric.md)
  A metric to record the amount of data that a performance test logically writes to storage.
- [class XCTApplicationLaunchMetric](xctapplicationlaunchmetric.md)
  A metric to record the application launch duration for a performance test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric)*