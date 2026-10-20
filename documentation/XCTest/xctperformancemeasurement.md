# XCTPerformanceMeasurement

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

A measurement from a single iteration of a performance test.

## Declaration

```swift
class XCTPerformanceMeasurement
```

```objc
@interface XCTPerformanceMeasurement : NSObject
```

## Topics

### Initializing a Measurement
- [init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String)](./xctperformancemeasurement/init%28identifier,displayname,doublevalue,unitsymbol%29.md)
  Initializes a performance measurement for a single iteration with the value and unit of measurement.
- [convenience init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String, polarity: XCTPerformanceMeasurement.Polarity)](./xctperformancemeasurement/init%28identifier,displayname,doublevalue,unitsymbol,polarity%29.md)
  Initializes a performance measurement for a single iteration with the value, unit of measurement, and polarity.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>)](./xctperformancemeasurement/init%28identifier,displayname,value%29.md)
  Initializes a performance measurement for a single iteration with the value.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>, polarity: XCTPerformanceMeasurement.Polarity)](./xctperformancemeasurement/init%28identifier,displayname,value,polarity%29.md)
  Initializes a performance measurement for a single iteration with the value and polarity.
### Identifying Measurements
- [var displayName: String](./xctperformancemeasurement/displayname.md)
  A human-readable name for a measurement.
- [var identifier: String](./xctperformancemeasurement/identifier.md)
  A unique identifier for a measurement.
### Accessing Measured Values
- [var doubleValue: Double](./xctperformancemeasurement/doublevalue.md)
  The measured value.
- [var unitSymbol: String](./xctperformancemeasurement/unitsymbol.md)
  A string that represents the unit of measurement.
- [var value: Measurement<Unit>](./xctperformancemeasurement/value.md)
  The measured value, including the unit of measure.
- [var polarity: XCTPerformanceMeasurement.Polarity](./xctperformancemeasurement/polarity-swift.property.md)
  A constant that states whether larger or smaller measurements, relative to a set baseline, indicate better performance.
- [XCTPerformanceMeasurement.Polarity](./xctperformancemeasurement/polarity-swift.enum.md)
  Constants that state whether larger or smaller measurements, relative to a set baseline, indicate better performance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Measurements
- [class XCTPerformanceMeasurementTimestamp](./xctperformancemeasurementtimestamp.md)
  A point in time that captures the start or finish of a performance test iteration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement)*