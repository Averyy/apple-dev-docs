# Performance Tests

**Framework**: Xctest

Gather metrics while running your code, and report a failure if the metrics become significantly worse than a baseline value.

## Topics

### Measuring Performance
- [Writing and running performance tests](../Xcode/writing-and-running-performance-tests.md)
  Repeatably gather metrics on the performance of your code.
### Measurement Options
- [class XCTMeasureOptions](xctmeasureoptions.md)
  Options to control the gathering of performance measurements during tests.
### Measurement Metrics
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
- [class XCTStorageMetric](xctstoragemetric.md)
  A metric to record the amount of data that a performance test logically writes to storage.
- [class XCTApplicationLaunchMetric](xctapplicationlaunchmetric.md)
  A metric to record the application launch duration for a performance test.
### Measurements
- [class XCTPerformanceMeasurement](xctperformancemeasurement.md)
  A measurement from a single iteration of a performance test.
- [class XCTPerformanceMeasurementTimestamp](xctperformancemeasurementtimestamp.md)
  A point in time that captures the start or finish of a performance test iteration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/performance-tests)*