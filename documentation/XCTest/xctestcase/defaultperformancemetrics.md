# defaultPerformanceMetrics

**Framework**: Xctest  
**Kind**: property

An array of default performance metrics the test records.

## Declaration

```swift
class var defaultPerformanceMetrics: [XCTPerformanceMetric] { get }
```

#### Discussion

When you call [`measure(_:)`](xctestcase/measure(_:).md), the test uses this property to determine which performance metrics to record. The default is an array that contains [`wallClockTime`](xctperformancemetric/wallclocktime.md). Subclasses of [`XCTestCase`](xctestcase.md) can override this method to change the behavior of [`measure(_:)`](xctestcase/measure(_:).md).

## See Also

- [static let wallClockTime: XCTPerformanceMetric](xctperformancemetric/wallclocktime.md)
  A performance metric that records the time in seconds to execute a block of code.
- [func measure(() -> Void)](xctestcase/measure(_:).md)
  Measures the performance of a block of code.
- [func measureMetrics([XCTPerformanceMetric], automaticallyStartMeasuring: Bool, for: () -> Void)](xctestcase/measuremetrics(_:automaticallystartmeasuring:for:).md)
  Measures the performance of a block of code, optionally deferring the starting point for measurement.
- [func measure(metrics: [any XCTMetric], block: () -> Void)](xctestcase/measure(metrics:block:).md)
  Records the selected metrics for a block of code.
- [func measure(metrics: [any XCTMetric], options: XCTMeasureOptions, block: () -> Void)](xctestcase/measure(metrics:options:block:).md)
  Records the selected metrics, using the specified measurement options, for a block of code.
- [func measure(options: XCTMeasureOptions, block: () -> Void)](xctestcase/measure(options:block:).md)
  Records the performance, using the specified measurement options, for a block of code.
- [func startMeasuring()](xctestcase/startmeasuring.md)
  Starts recording performance metrics within a block of code.
- [func stopMeasuring()](xctestcase/stopmeasuring.md)
  Ends recording performance metrics within a block of code.
- [class var defaultMetrics: [any XCTMetric]](xctestcase/defaultmetrics.md)
  An array of default metrics the test uses to record performance.
- [class var defaultMeasureOptions: XCTMeasureOptions](xctestcase/defaultmeasureoptions.md)
  The default measurement options the test uses to record performance.
- [struct XCTPerformanceMetric](xctperformancemetric.md)
  Performance metrics that the test records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/defaultperformancemetrics)*