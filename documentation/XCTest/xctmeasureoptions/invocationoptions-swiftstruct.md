# XCTMeasureOptions.InvocationOptions

**Framework**: XCTest  
**Kind**: struct

Test measurement options that control how measurement starts and stops.

## Declaration

```swift
struct InvocationOptions
```

## Topics

### Measurement Options
- [static var manuallyStart: XCTMeasureOptions.InvocationOptions](xctmeasureoptions/invocationoptions-swift.struct/manuallystart.md)
  An invocation option that specifies that the test starts taking measurements when the `startMeasuring()` function is called.
- [static var manuallyStop: XCTMeasureOptions.InvocationOptions](xctmeasureoptions/invocationoptions-swift.struct/manuallystop.md)
  An invocation option that specifies that the test stops taking measurements when the `stopMeasuring()` function is called.
### Initializers
- [init(rawValue: UInt)](xctmeasureoptions/invocationoptions-swift.struct/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var invocationOptions: XCTMeasureOptions.InvocationOptions](xctmeasureoptions/invocationoptions-swift.property.md)
  Options that define whether measurement is automatically or manually controlled.
- [var iterationCount: Int](xctmeasureoptions/iterationcount.md)
  The number of times the performance test measures its block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmeasureoptions/invocationoptions-swift.struct)*