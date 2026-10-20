# init(identifier:displayName:doubleValue:unitSymbol:polarity:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes a performance measurement for a single iteration with the value, unit of measurement, and polarity.

## Declaration

```swift
convenience init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String, polarity: XCTPerformanceMeasurement.Polarity)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier displayName:(NSString *) displayName doubleValue:(double) doubleValue unitSymbol:(NSString *) unitSymbol polarity:(XCTPerformanceMeasurementPolarity) polarity;
```

## Parameters

- `identifier`: A unique identifier for the measurement.
- `displayName`: A human-readable name for the measurement.
- `doubleValue`: A value for the measurement.
- `unitSymbol`: A string that represents the unit of measurement, such as seconds.
- `polarity`: A value that states whether larger or smaller measurements, relative to a set baseline, indicate better performance.

## See Also

### Initializing a Measurement
- [init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String)](./init%28identifier,displayname,doublevalue,unitsymbol%29.md)
  Initializes a performance measurement for a single iteration with the value and unit of measurement.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>)](./init%28identifier,displayname,value%29.md)
  Initializes a performance measurement for a single iteration with the value.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>, polarity: XCTPerformanceMeasurement.Polarity)](./init%28identifier,displayname,value,polarity%29.md)
  Initializes a performance measurement for a single iteration with the value and polarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/init(identifier:displayname:doublevalue:unitsymbol:polarity:))*