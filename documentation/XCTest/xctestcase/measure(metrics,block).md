# measure(metrics:block:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Records the selected metrics for a block of code.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func measure(metrics: [any XCTMetric], block: () -> Void)
```

```objc
- (void) measureWithMetrics:(NSArray<id<XCTMetric>> *) metrics block:(void (^)()) block;
```

## Parameters

- `metrics`: An array of metrics to measure, like CPU, memory, or elapsed time.
- `block`: A block whose performance is measured.

## See Also

### Measuring Performance
- [func measure(() -> Void)](./measure%28_%29.md)
  Measures the performance of a block of code.
- [func measureMetrics([XCTPerformanceMetric], automaticallyStartMeasuring: Bool, for: () -> Void)](./measuremetrics%28_,automaticallystartmeasuring,for%29.md)
  Measures the performance of a block of code, optionally deferring the starting point for measurement.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/measure(metrics:block:))*