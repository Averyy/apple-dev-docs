# XCTPerformanceMeasurement.Polarity

**Framework**: XCTest  
**Kind**: enum

Constants that state whether larger or smaller measurements, relative to a set baseline, indicate better performance.

## Declaration

```swift
enum Polarity
```

## Topics

### Polarity Types
- [XCTPerformanceMeasurement.Polarity.prefersLarger](xctperformancemeasurement/polarity-swift.enum/preferslarger.md)
  A performance measurement where a larger value, relative to a set baseline, indicates better performance.
- [XCTPerformanceMeasurement.Polarity.prefersSmaller](xctperformancemeasurement/polarity-swift.enum/preferssmaller.md)
  A performance measurement where a smaller value, relative to a set baseline, indicates better performance.
- [XCTPerformanceMeasurement.Polarity.unspecified](xctperformancemeasurement/polarity-swift.enum/unspecified.md)
  A performance measurement that doesn’t specify whether a larger or smaller value, relative to a set baseline, indicates better performance.
### Initializers
- [init?(rawValue: Int)](xctperformancemeasurement/polarity-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var doubleValue: Double](xctperformancemeasurement/doublevalue.md)
  The measured value.
- [var unitSymbol: String](xctperformancemeasurement/unitsymbol.md)
  A string that represents the unit of measurement.
- [var value: Measurement<Unit>](xctperformancemeasurement/value.md)
  The measured value, including the unit of measure.
- [var polarity: XCTPerformanceMeasurement.Polarity](xctperformancemeasurement/polarity-swift.property.md)
  A constant that states whether larger or smaller measurements, relative to a set baseline, indicate better performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/polarity-swift.enum)*