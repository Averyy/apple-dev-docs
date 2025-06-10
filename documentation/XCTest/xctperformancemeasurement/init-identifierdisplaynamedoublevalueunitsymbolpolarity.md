# init(identifier:displayName:doubleValue:unitSymbol:polarity:)

**Framework**: XCTest  
**Kind**: init

Initializes a performance measurement for a single iteration with the value, unit of measurement, and polarity.

## Declaration

```swift
convenience init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String, polarity: XCTPerformanceMeasurement.Polarity)
```

## Parameters

- `identifier`: A unique identifier for the measurement.
- `displayName`: A human-readable name for the measurement.
- `doubleValue`: A value for the measurement.
- `unitSymbol`: A string that represents the unit of measurement, such as seconds.
- `polarity`: A value that states whether larger or smaller measurements, relative to a set baseline, indicate better performance.

## See Also

- [init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String)](xctperformancemeasurement/init(identifier:displayname:doublevalue:unitsymbol:).md)
  Initializes a performance measurement for a single iteration with the value and unit of measurement.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>)](xctperformancemeasurement/init(identifier:displayname:value:).md)
  Initializes a performance measurement for a single iteration with the value.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>, polarity: XCTPerformanceMeasurement.Polarity)](xctperformancemeasurement/init(identifier:displayname:value:polarity:).md)
  Initializes a performance measurement for a single iteration with the value and polarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/init(identifier:displayname:doublevalue:unitsymbol:polarity:))*