# XCTMetric

**Framework**: XCTest  
**Kind**: protocol

A protocol that defines the methods that objects must provide when gathering metrics during performance tests.

## Declaration

```swift
protocol XCTMetric : NSCopying, NSObjectProtocol
```

#### Overview

Objects that gather metrics during performance tests must conform to `XCTMetric`. Before you create your own conforming objects, first use the metrics classes that `XCTest` supplies.

## Topics

### Recording Metrics
- [func willBeginMeasuring()](xctmetric/willbeginmeasuring.md)
  A method that XCTest calls when it’s ready to begin running the measured code.
- [func didStopMeasuring()](xctmetric/didstopmeasuring.md)
  A method that XCTest calls when it has finished running the measured code.
### Reporting Gathered Metrics
- [func reportMeasurements(from: XCTPerformanceMeasurementTimestamp, to: XCTPerformanceMeasurementTimestamp) throws -> [XCTPerformanceMeasurement]](xctmetric/reportmeasurements(from:to:).md)
  Reports the measurements gathered for a metric between specific timestamps.

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [XCTApplicationLaunchMetric](xctapplicationlaunchmetric.md)
- [XCTCPUMetric](xctcpumetric.md)
- [XCTClockMetric](xctclockmetric.md)
- [XCTHitchMetric](xcthitchmetric.md)
- [XCTMemoryMetric](xctmemorymetric.md)
- [XCTOSSignpostMetric](xctossignpostmetric.md)
- [XCTStorageMetric](xctstoragemetric.md)

## See Also

- [class XCTCPUMetric](xctcpumetric.md)
  A metric to record information about CPU activity during a performance test.
- [class XCTClockMetric](xctclockmetric.md)
  A metric to record the time that elapses during a performance test.
- [class XCTMemoryMetric](xctmemorymetric.md)
  A metric to record the physical memory that a performance test uses.
- [class XCTOSSignpostMetric](xctossignpostmetric.md)
  A metric to record the time that a performance test spends executing a signposted region of code.
- [class XCTStorageMetric](xctstoragemetric.md)
  A metric to record the amount of data that a performance test logically writes to storage.
- [class XCTApplicationLaunchMetric](xctapplicationlaunchmetric.md)
  A metric to record the application launch duration for a performance test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmetric)*