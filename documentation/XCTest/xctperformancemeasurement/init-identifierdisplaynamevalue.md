# init(identifier:displayName:value:)

**Framework**: Xctest  
**Kind**: init

Initializes a performance measurement for a single iteration with the value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(identifier: String, displayName: String, value: Measurement<Unit>)
```

## Parameters

- `identifier`: A unique identifier for the measurement.
- `displayName`: A human-readable name for the measurement.
- `value`: A value for the measurement.

## See Also

- [init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String)](xctperformancemeasurement/init(identifier:displayname:doublevalue:unitsymbol:).md)
  Initializes a performance measurement for a single iteration with the value and unit of measurement.
- [convenience init(identifier: String, displayName: String, doubleValue: Double, unitSymbol: String, polarity: XCTPerformanceMeasurement.Polarity)](xctperformancemeasurement/init(identifier:displayname:doublevalue:unitsymbol:polarity:).md)
  Initializes a performance measurement for a single iteration with the value, unit of measurement, and polarity.
- [convenience init(identifier: String, displayName: String, value: Measurement<Unit>, polarity: XCTPerformanceMeasurement.Polarity)](xctperformancemeasurement/init(identifier:displayname:value:polarity:).md)
  Initializes a performance measurement for a single iteration with the value and polarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/init(identifier:displayname:value:))*