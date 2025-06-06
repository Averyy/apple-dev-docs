# init(identifier:displayName:doubleValue:unitSymbol:)

**Framework**: Xctest  
**Kind**: init

Initializes a performance measurement for a single iteration with the value and unit of measurement.

## Declaration

```swift
init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String)
```

## Parameters

- `identifier`: A unique identifier for the measurement.
- `displayName`: A human-readable name for the measurement.
- `doubleValue`: A value for the measurement.
- `unitSymbol`: A string that represents the unit of measurement, such as seconds.

## See Also

- [convenience init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String, polarity: XCTPerformanceMeasurement.Polarity)](xctperformancemeasurement/init(identifier:displayname:doublevalue:unitsymbol:polarity:).md)
  Initializes a performance measurement for a single iteration with the value, unit of measurement, and polarity.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>)](xctperformancemeasurement/init(identifier:displayname:value:).md)
  Initializes a performance measurement for a single iteration with the value.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>, polarity: XCTPerformanceMeasurement.Polarity)](xctperformancemeasurement/init(identifier:displayname:value:polarity:).md)
  Initializes a performance measurement for a single iteration with the value and polarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/init(identifier:displayname:doublevalue:unitsymbol:))*