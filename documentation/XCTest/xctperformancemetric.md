# XCTPerformanceMetric

**Framework**: XCTest  
**Kind**: struct  
**Role**: Structure

Performance metrics that the test records.

## Declaration

```swift
struct XCTPerformanceMetric
```

```c
typedef NSString * XCTPerformanceMetric;
```

## Topics

### Measuring Elapsed Time
- [static let wallClockTime: XCTPerformanceMetric](./xctperformancemetric/wallclocktime.md)
  A performance metric that records the time in seconds to execute a block of code.
### Initializing an Item
- [init(String)](./xctperformancemetric/init%28_%29.md)
  Creates a new instance with the specified raw value.
- [init(rawValue: String)](./xctperformancemetric/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Measuring Performance
- [func measure(() -> Void)](./xctestcase/measure%28_%29.md)
  Measures the performance of a block of code.
- [func measureMetrics([XCTPerformanceMetric], automaticallyStartMeasuring: Bool, for: () -> Void)](./xctestcase/measuremetrics%28_,automaticallystartmeasuring,for%29.md)
  Measures the performance of a block of code, optionally deferring the starting point for measurement.
- [func measure(metrics: [any XCTMetric], block: () -> Void)](./xctestcase/measure%28metrics,block%29.md)
  Records the selected metrics for a block of code.
- [func measure(metrics: [any XCTMetric], options: XCTMeasureOptions, block: () -> Void)](./xctestcase/measure%28metrics,options,block%29.md)
  Records the selected metrics, using the specified measurement options, for a block of code.
- [func measure(options: XCTMeasureOptions, block: () -> Void)](./xctestcase/measure%28options,block%29.md)
  Records the performance, using the specified measurement options, for a block of code.
- [func startMeasuring()](./xctestcase/startmeasuring%28%29.md)
  Starts recording performance metrics within a block of code.
- [func stopMeasuring()](./xctestcase/stopmeasuring%28%29.md)
  Ends recording performance metrics within a block of code.
- [class var defaultPerformanceMetrics: [XCTPerformanceMetric]](./xctestcase/defaultperformancemetrics.md)
  An array of default performance metrics the test records.
- [class var defaultMetrics: [any XCTMetric]](./xctestcase/defaultmetrics.md)
  An array of default metrics the test uses to record performance.
- [class var defaultMeasureOptions: XCTMeasureOptions](./xctestcase/defaultmeasureoptions.md)
  The default measurement options the test uses to record performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemetric)*