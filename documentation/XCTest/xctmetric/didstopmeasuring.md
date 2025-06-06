# didStopMeasuring()

**Framework**: Xctest  
**Kind**: method

A method that XCTest calls when it has finished running the measured code.

## Declaration

```swift
optional func didStopMeasuring()
```

#### Discussion

XCTest calls this method when it has finished running the code in the performance test’s `measure()` or `measure(metrics:)` block. It calls the method once for each iteration of a performance test. Use this method to finish gathering measurements.

## See Also

- [func willBeginMeasuring()](xctmetric/willbeginmeasuring.md)
  A method that XCTest calls when it’s ready to begin running the measured code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmetric/didstopmeasuring())*