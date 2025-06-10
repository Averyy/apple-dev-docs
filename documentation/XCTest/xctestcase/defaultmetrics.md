# defaultMetrics

**Framework**: XCTest  
**Kind**: property

An array of default metrics the test uses to record performance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class var defaultMetrics: [any XCTMetric] { get }
```

#### Discussion

When you call [`measure(options:block:)`](xctestcase/measure(options:block:).md), the test uses this property to determine which metrics to record. The default is an array that contains [`XCTClockMetric`](xctclockmetric.md). Subclasses of [`XCTestCase`](xctestcase.md) can override this property to change the default metrics.

## See Also

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
- [class var defaultPerformanceMetrics: [XCTPerformanceMetric]](xctestcase/defaultperformancemetrics.md)
  An array of default performance metrics the test records.
- [class var defaultMeasureOptions: XCTMeasureOptions](xctestcase/defaultmeasureoptions.md)
  The default measurement options the test uses to record performance.
- [struct XCTPerformanceMetric](xctperformancemetric.md)
  Performance metrics that the test records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/defaultmetrics)*