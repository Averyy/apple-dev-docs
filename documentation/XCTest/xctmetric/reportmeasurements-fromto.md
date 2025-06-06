# reportMeasurements(from:to:)

**Framework**: Xctest  
**Kind**: method  
**Required**: Yes

Reports the measurements gathered for a metric between specific timestamps.

## Declaration

```swift
func reportMeasurements(from startTime: XCTPerformanceMeasurementTimestamp, to endTime: XCTPerformanceMeasurementTimestamp) throws -> [XCTPerformanceMeasurement]
```

#### Return Value

An array of the measurements gathered by this metric during the requested interval.

#### Discussion

Report the measurements gathered during the execution of measured code in a performance test. Use the `startTime` and `endTime` parameters to refine the accuracy of the reported measurements.

## Parameters

- `startTime`: A timestamp that represents the time at which the measured code began to execute.
- `endTime`: A timestamp that represents the time at which the measured code finished executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmetric/reportmeasurements(from:to:))*