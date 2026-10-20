# init(identifier:displayName:value:polarity:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes a performance measurement for a single iteration with the value and polarity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(identifier: String, displayName: String, value: Measurement<Unit>, polarity: XCTPerformanceMeasurement.Polarity)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier displayName:(NSString *) displayName value:(NSMeasurement *) value polarity:(XCTPerformanceMeasurementPolarity) polarity;
```

## Parameters

- `identifier`: A unique identifier for the measurement.
- `displayName`: A human-readable name for the measurement.
- `value`: A value for the measurement.
- `polarity`: A value that states whether larger or smaller measurements, relative to a set baseline, indicate better performance.

## See Also

### Initializing a Measurement
- [init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String)](./init%28identifier,displayname,doublevalue,unitsymbol%29.md)
  Initializes a performance measurement for a single iteration with the value and unit of measurement.
- [convenience init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String, polarity: XCTPerformanceMeasurement.Polarity)](./init%28identifier,displayname,doublevalue,unitsymbol,polarity%29.md)
  Initializes a performance measurement for a single iteration with the value, unit of measurement, and polarity.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>)](./init%28identifier,displayname,value%29.md)
  Initializes a performance measurement for a single iteration with the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/init(identifier:displayname:value:polarity:))*