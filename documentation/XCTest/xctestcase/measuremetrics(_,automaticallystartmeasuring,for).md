# measureMetrics(_:automaticallyStartMeasuring:for:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Measures the performance of a block of code, optionally deferring the starting point for measurement.

## Declaration

```swift
func measureMetrics(_ metrics: [XCTPerformanceMetric], automaticallyStartMeasuring: Bool, for block: () -> Void)
```

```objc
- (void) measureMetrics:(NSArray<NSString *> *) metrics automaticallyStartMeasuring:(BOOL) automaticallyStartMeasuring forBlock:(void (^)()) block;
```

#### Discussion

Call this method from within a test method to measure the performance of a block of code. This method provides more granular control over performance measurement than the  [`measure(_:)`](./measure%28_%29.md) method, and should be used when you need to customize the points at which measurement starts and ends within the block, or wish to measure multiple metrics for the block.

Performance measurement must be started and stopped exactly once within the block. As a result:

- If `automaticallyStartMeasuring` is [`true`](../../Swift/true.md) and [`startMeasuring()`](./startmeasuring%28%29.md) is called inside the block, the test will fail.
- If `automaticallyStartMeasuring` is [`false`](../../Swift/false.md), [`startMeasuring()`](./startmeasuring%28%29.md) must be called once and only once before the end of the block, or the test will fail.
- If [`stopMeasuring()`](./stopmeasuring%28%29.md) is called multiple times during the block the test will fail.

## Parameters

- `metrics`: An array of performance metrics to measure. Each metric is measured across calls to the block. Pass [`wallClockTime`](../xctperformancemetric/wallclocktime.md) to measure the number of seconds taken to execute the  block of code.
- `automaticallyStartMeasuring`: If [`false`](../../Swift/false.md), measurements will not be taken until [`startMeasuring()`](./startmeasuring%28%29.md) is called inside the block.
- `block`: A block whose performance is measured.

## See Also

### Related Documentation
- [static let wallClockTime: XCTPerformanceMetric](../xctperformancemetric/wallclocktime.md)
  A performance metric that records the time in seconds to execute a block of code.
### Measuring Performance
- [func measure(() -> Void)](./measure%28_%29.md)
  Measures the performance of a block of code.
- [func measure(metrics: [any XCTMetric], block: () -> Void)](./measure%28metrics,block%29.md)
  Records the selected metrics for a block of code.
- [func measure(metrics: [any XCTMetric], options: XCTMeasureOptions, block: () -> Void)](./measure%28metrics,options,block%29.md)
  Records the selected metrics, using the specified measurement options, for a block of code.
- [func measure(options: XCTMeasureOptions, block: () -> Void)](./measure%28options,block%29.md)
  Records the performance, using the specified measurement options, for a block of code.
- [func startMeasuring()](./startmeasuring%28%29.md)
  Starts recording performance metrics within a block of code.
- [func stopMeasuring()](./stopmeasuring%28%29.md)
  Ends recording performance metrics within a block of code.
- [class var defaultPerformanceMetrics: [XCTPerformanceMetric]](./defaultperformancemetrics.md)
  An array of default performance metrics the test records.
- [class var defaultMetrics: [any XCTMetric]](./defaultmetrics.md)
  An array of default metrics the test uses to record performance.
- [class var defaultMeasureOptions: XCTMeasureOptions](./defaultmeasureoptions.md)
  The default measurement options the test uses to record performance.
- [struct XCTPerformanceMetric](../xctperformancemetric.md)
  Performance metrics that the test records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/measuremetrics(_:automaticallystartmeasuring:for:))*