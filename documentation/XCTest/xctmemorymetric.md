# XCTMemoryMetric

**Framework**: XCTest  
**Kind**: class

A metric to record the physical memory that a performance test uses.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class XCTMemoryMetric
```

#### Overview

`XCTMemoryMetric` compares the memory use before and after running the block argument to [`measure(metrics:block:)`](xctestcase/measure(metrics:block:).md), and reports the difference.

## Topics

### Initializers
- [init()](xctmemorymetric/init.md)
  Initializes a metric that measures memory use in the current process.
- [init(application: XCUIApplication)](xctmemorymetric/init(application:).md)
  Initializes a metric that measures memory use in the target app.

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
- [class XCTOSSignpostMetric](xctossignpostmetric.md)
  A metric to record the time that a performance test spends executing a signposted region of code.
- [class XCTStorageMetric](xctstoragemetric.md)
  A metric to record the amount of data that a performance test logically writes to storage.
- [class XCTApplicationLaunchMetric](xctapplicationlaunchmetric.md)
  A metric to record the application launch duration for a performance test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmemorymetric)*