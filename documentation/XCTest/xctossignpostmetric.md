# XCTOSSignpostMetric

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

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

```objc
@interface XCTOSSignpostMetric : NSObject
```

#### Overview

This metric captures the time that elapses between the [`begin`](../os/ossignposttype/begin.md) and [`end`](../os/ossignposttype/end.md) events for a specific named [`os_signpost(_:dso:log:name:signpostID:)`](../os/os_signpost%28_,dso,log,name,signpostid%29-2oz8u.md) region. It doesn’t record any results when there isn’t a matching pair of `begin` and `end` events.

## Topics

### Measuring Specific Signposts
- [init(subsystem: String, category: String, name: String)](./xctossignpostmetric/init%28subsystem,category,name%29.md)
  Creates a metric to record a specific signpost.
### Measuring Navigation Transitions
- [class var customNavigationTransitionMetric: any XCTMetric](./xctossignpostmetric/customnavigationtransitionmetric.md)
  A metric that records the duration of custom navigation transitions between views.
- [class var navigationTransitionMetric: any XCTMetric](./xctossignpostmetric/navigationtransitionmetric.md)
  A metric that records the duration of navigation transitions between views.
### Measuring Scrolling Properties
- [class var scrollingAndDecelerationMetric: any XCTMetric](./xctossignpostmetric/scrollinganddecelerationmetric.md)
  A metric that records scroll-dragging and deceleration animations.
### Deprecated
- [class var applicationLaunch: XCTOSSignpostMetric](./xctossignpostmetric/applicationlaunch.md)
  A metric that records the time that elapses during app launch.
- [class var scrollDecelerationMetric: any XCTMetric](./xctossignpostmetric/scrolldecelerationmetric.md)
  A metric that records scroll deceleration animations.
- [class var scrollDraggingMetric: any XCTMetric](./xctossignpostmetric/scrolldraggingmetric.md)
  A metric that records scroll-dragging animations.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [XCTMetric](./xctmetric.md)

## See Also

### Measurement Metrics
- [protocol XCTMetric](./xctmetric.md)
  A protocol that defines the methods that objects must provide when gathering metrics during performance tests.
- [class XCTCPUMetric](./xctcpumetric.md)
  A metric to record information about CPU activity during a performance test.
- [class XCTClockMetric](./xctclockmetric.md)
  A metric to record the time that elapses during a performance test.
- [class XCTHitchMetric](./xcthitchmetric.md)
  A metric to measure the number of hitches your UI encounters in a performance test.
- [class XCTMemoryMetric](./xctmemorymetric.md)
  A metric to record the physical memory that a performance test uses.
- [class XCTStorageMetric](./xctstoragemetric.md)
  A metric to record the amount of data that a performance test logically writes to storage.
- [class XCTApplicationLaunchMetric](./xctapplicationlaunchmetric.md)
  A metric to record the application launch duration for a performance test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric)*