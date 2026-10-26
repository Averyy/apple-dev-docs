# XCTMeasureOptions.InvocationOptions

**Framework**: XCTest  
**Kind**: struct  
**Role**: Structure

Test measurement options that control how measurement starts and stops.

## Declaration

```swift
struct InvocationOptions
```

```c
enum XCTMeasurementInvocationOptions : NSUInteger;
```

## Topics

### Measurement Options
- [static var manuallyStart: XCTMeasureOptions.InvocationOptions](./invocationoptions-swift.struct/manuallystart.md)
  An invocation option that specifies that the test starts taking measurements when the `startMeasuring()` function is called.
- [static var manuallyStop: XCTMeasureOptions.InvocationOptions](./invocationoptions-swift.struct/manuallystop.md)
  An invocation option that specifies that the test stops taking measurements when the `stopMeasuring()` function is called.
### Initializers
- [init(rawValue: UInt)](./invocationoptions-swift.struct/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
### Enumeration Cases
- [XCTMeasurementInvocationNone](../xctmeasurementinvocationoptions/xctmeasurementinvocationnone.md)
  An invocation option that specifies that the test automatically takes measurements at the beginning and ending of a measure block.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Using Option Details
- [var invocationOptions: XCTMeasureOptions.InvocationOptions](./invocationoptions-swift.property.md)
  Options that define whether measurement is automatically or manually controlled.
- [var iterationCount: Int](./iterationcount.md)
  The number of times the performance test measures its block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmeasureoptions/invocationoptions-swift.struct)*