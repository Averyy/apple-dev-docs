# startMeasuring()

**Framework**: Xctest  
**Kind**: method

Starts recording performance metrics within a block of code.

## Declaration

```swift
func startMeasuring()
```

#### Discussion

Call this method to start the measurement of metrics by the [`measureMetrics(_:automaticallyStartMeasuring:for:)`](xctestcase/measuremetrics(_:automaticallystartmeasuring:for:).md) method. Measurement will start immediately after this method is called from within the measured block.

> **Note**:  You must call [`measureMetrics(_:automaticallyStartMeasuring:for:)`](xctestcase/measuremetrics(_:automaticallystartmeasuring:for:).md) with an `automaticallyStartMeasuring` value of [`false`](https://developer.apple.com/documentation/swift/false) in order to set a custom start point with [`startMeasuring()`](xctestcase/startmeasuring().md).

 You must call [`measureMetrics(_:automaticallyStartMeasuring:for:)`](xctestcase/measuremetrics(_:automaticallystartmeasuring:for:).md) with an `automaticallyStartMeasuring` value of [`false`](https://developer.apple.com/documentation/swift/false) in order to set a custom start point with [`startMeasuring()`](xctestcase/startmeasuring().md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/startmeasuring())*