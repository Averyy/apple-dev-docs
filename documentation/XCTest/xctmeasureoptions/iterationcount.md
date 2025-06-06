# iterationCount

**Framework**: Xctest  
**Kind**: property

The number of times the performance test measures its block.

## Declaration

```swift
var iterationCount: Int { get set }
```

#### Discussion

A performance test runs its block `iterationCount+1` times, ignoring the first iteration and recording metrics for the remaining iterations. The test ignores the first iteration to reduce measurement variance associated with “warming up” caches and other first-run behavior.

## See Also

- [var invocationOptions: XCTMeasureOptions.InvocationOptions](xctmeasureoptions/invocationoptions-swift.property.md)
  Options that define whether measurement is automatically or manually controlled.
- [XCTMeasureOptions.InvocationOptions](xctmeasureoptions/invocationoptions-swift.struct.md)
  Test measurement options that control how measurement starts and stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmeasureoptions/iterationcount)*