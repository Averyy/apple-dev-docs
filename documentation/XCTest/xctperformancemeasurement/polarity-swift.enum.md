# XCTPerformanceMeasurement.Polarity

**Framework**: XCTest  
**Kind**: enum  
**Role**: Enumeration

Constants that state whether larger or smaller measurements, relative to a set baseline, indicate better performance.

## Declaration

```swift
enum Polarity
```

```c
enum XCTPerformanceMeasurementPolarity : NSInteger;
```

## Topics

### Polarity Types
- [XCTPerformanceMeasurement.Polarity.prefersLarger](./polarity-swift.enum/preferslarger.md)
  A performance measurement where a larger value, relative to a set baseline, indicates better performance.
- [XCTPerformanceMeasurement.Polarity.prefersSmaller](./polarity-swift.enum/preferssmaller.md)
  A performance measurement where a smaller value, relative to a set baseline, indicates better performance.
- [XCTPerformanceMeasurement.Polarity.unspecified](./polarity-swift.enum/unspecified.md)
  A performance measurement that doesn’t specify whether a larger or smaller value, relative to a set baseline, indicates better performance.
### Initializers
- [init?(rawValue: Int)](./polarity-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Measured Values
- [var doubleValue: Double](./doublevalue.md)
  The measured value.
- [var unitSymbol: String](./unitsymbol.md)
  A string that represents the unit of measurement.
- [var value: Measurement<Unit>](./value.md)
  The measured value, including the unit of measure.
- [var polarity: XCTPerformanceMeasurement.Polarity](./polarity-swift.property.md)
  A constant that states whether larger or smaller measurements, relative to a set baseline, indicate better performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/polarity-swift.enum)*