# measureMetrics(_:automaticallyStartMeasuring:for:)

**Framework**: XCTest  
**Kind**: method

Measures the performance of a block of code, optionally deferring the starting point for measurement.

## Declaration

```swift
func measureMetrics(_ metrics: [XCTPerformanceMetric], automaticallyStartMeasuring: Bool, for block: () -> Void)
```

#### Discussion

Call this method from within a test method to measure the performance of a block of code. This method provides more granular control over performance measurement than the  [`measure(_:)`](xctestcase/measure(_:).md) method, and should be used when you need to customize the points at which measurement starts and ends within the block, or wish to measure multiple metrics for the block.

Performance measurement must be started and stopped exactly once within the block. As a result:

- If `automaticallyStartMeasuring` is [`true`](https://developer.apple.com/documentation/swift/true) and [`startMeasuring()`](xctestcase/startmeasuring().md) is called inside the block, the test will fail.
- If `automaticallyStartMeasuring` is [`false`](https://developer.apple.com/documentation/swift/false), [`startMeasuring()`](xctestcase/startmeasuring().md) must be called once and only once before the end of the block, or the test will fail.
- If [`stopMeasuring()`](xctestcase/stopmeasuring().md) is called multiple times during the block the test will fail.

## Parameters

- `metrics`: An array of performance metrics to measure. Each metric is measured across calls to the block. Pass   to measure the number of seconds taken to execute the  block of code.
- `automaticallyStartMeasuring`: If  , measurements will not be taken until   is called inside the block.
- `block`: A block whose performance is measured.

## See Also

- [static let wallClockTime: XCTPerformanceMetric](xctperformancemetric/wallclocktime.md)
  A performance metric that records the time in seconds to execute a block of code.
- [func measure(() -> Void)](xctestcase/measure(_:).md)
  Measures the performance of a block of code.
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
- [class var defaultMetrics: [any XCTMetric]](xctestcase/defaultmetrics.md)
  An array of default metrics the test uses to record performance.
- [class var defaultMeasureOptions: XCTMeasureOptions](xctestcase/defaultmeasureoptions.md)
  The default measurement options the test uses to record performance.
- [struct XCTPerformanceMetric](xctperformancemetric.md)
  Performance metrics that the test records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/measuremetrics(_:automaticallystartmeasuring:for:))*