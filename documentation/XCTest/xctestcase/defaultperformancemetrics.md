# defaultPerformanceMetrics

**Framework**: XCTest  
**Kind**: property  
**Role**: Type Property

An array of default performance metrics the test records.

## Declaration

```swift
class var defaultPerformanceMetrics: [XCTPerformanceMetric] { get }
```

```objc
@property (class, copy, readonly) NSArray<NSString *> * defaultPerformanceMetrics;
```

#### Discussion

When you call [`measure(_:)`](./measure%28_%29.md), the test uses this property to determine which performance metrics to record. The default is an array that contains [`wallClockTime`](../xctperformancemetric/wallclocktime.md). Subclasses of [`XCTestCase`](../xctestcase.md) can override this method to change the behavior of [`measure(_:)`](./measure%28_%29.md).

## See Also

### Related Documentation
- [static let wallClockTime: XCTPerformanceMetric](../xctperformancemetric/wallclocktime.md)
  A performance metric that records the time in seconds to execute a block of code.
### Measuring Performance
- [func measure(() -> Void)](./measure%28_%29.md)
  Measures the performance of a block of code.
- [func measureMetrics([XCTPerformanceMetric], automaticallyStartMeasuring: Bool, for: () -> Void)](./measuremetrics%28_,automaticallystartmeasuring,for%29.md)
  Measures the performance of a block of code, optionally deferring the starting point for measurement.
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
- [class var defaultMetrics: [any XCTMetric]](./defaultmetrics.md)
  An array of default metrics the test uses to record performance.
- [class var defaultMeasureOptions: XCTMeasureOptions](./defaultmeasureoptions.md)
  The default measurement options the test uses to record performance.
- [struct XCTPerformanceMetric](../xctperformancemetric.md)
  Performance metrics that the test records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/defaultperformancemetrics)*