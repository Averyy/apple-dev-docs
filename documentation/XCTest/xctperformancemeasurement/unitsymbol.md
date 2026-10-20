# unitSymbol

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

A string that represents the unit of measurement.

## Declaration

```swift
var unitSymbol: String { get }
```

```objc
@property (copy, readonly) NSString * unitSymbol;
```

## See Also

### Accessing Measured Values
- [var doubleValue: Double](./doublevalue.md)
  The measured value.
- [var value: Measurement<Unit>](./value.md)
  The measured value, including the unit of measure.
- [var polarity: XCTPerformanceMeasurement.Polarity](./polarity-swift.property.md)
  A constant that states whether larger or smaller measurements, relative to a set baseline, indicate better performance.
- [XCTPerformanceMeasurement.Polarity](./polarity-swift.enum.md)
  Constants that state whether larger or smaller measurements, relative to a set baseline, indicate better performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/unitsymbol)*