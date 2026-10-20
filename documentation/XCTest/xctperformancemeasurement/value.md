# value

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The measured value, including the unit of measure.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var value: Measurement<Unit> { get }
```

```objc
@property (copy, readonly) NSMeasurement * value;
```

## See Also

### Accessing Measured Values
- [var doubleValue: Double](./doublevalue.md)
  The measured value.
- [var unitSymbol: String](./unitsymbol.md)
  A string that represents the unit of measurement.
- [var polarity: XCTPerformanceMeasurement.Polarity](./polarity-swift.property.md)
  A constant that states whether larger or smaller measurements, relative to a set baseline, indicate better performance.
- [XCTPerformanceMeasurement.Polarity](./polarity-swift.enum.md)
  Constants that state whether larger or smaller measurements, relative to a set baseline, indicate better performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/value)*