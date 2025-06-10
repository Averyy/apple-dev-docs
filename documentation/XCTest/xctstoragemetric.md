# XCTStorageMetric

**Framework**: XCTest  
**Kind**: class

A metric to record the amount of data that a performance test logically writes to storage.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class XCTStorageMetric
```

#### Overview

`XCTStorageMetric` records the amount of data logically written to the disk in the block argument to [`measure(metrics:block:)`](xctestcase/measure(metrics:block:).md). The logical size of data written is the number of bytes in all requests to write to the disk. The logical size can be different from the size of physically written data, based on how the file system organizes data, and the fact that the disk controller replaces content in fixed-size blocks.

## Topics

### Initializers
- [init()](xctstoragemetric/init.md)
  Creates a metric for measuring disk use in a process.
- [init(application: XCUIApplication)](xctstoragemetric/init(application:).md)
  Creates a metric for measuring disk use in the requested app.

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
- [class XCTOSSignpostMetric](xctossignpostmetric.md)
  A metric to record the time that a performance test spends executing a signposted region of code.
- [class XCTApplicationLaunchMetric](xctapplicationlaunchmetric.md)
  A metric to record the application launch duration for a performance test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctstoragemetric)*