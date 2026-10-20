# init(identifier:displayName:doubleValue:unitSymbol:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes a performance measurement for a single iteration with the value and unit of measurement.

## Declaration

```swift
init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier displayName:(NSString *) displayName doubleValue:(double) doubleValue unitSymbol:(NSString *) unitSymbol;
```

## Parameters

- `identifier`: A unique identifier for the measurement.
- `displayName`: A human-readable name for the measurement.
- `doubleValue`: A value for the measurement.
- `unitSymbol`: A string that represents the unit of measurement, such as seconds.

## See Also

### Initializing a Measurement
- [convenience init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String, polarity: XCTPerformanceMeasurement.Polarity)](./init%28identifier,displayname,doublevalue,unitsymbol,polarity%29.md)
  Initializes a performance measurement for a single iteration with the value, unit of measurement, and polarity.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>)](./init%28identifier,displayname,value%29.md)
  Initializes a performance measurement for a single iteration with the value.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>, polarity: XCTPerformanceMeasurement.Polarity)](./init%28identifier,displayname,value,polarity%29.md)
  Initializes a performance measurement for a single iteration with the value and polarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/init(identifier:displayname:doublevalue:unitsymbol:))*