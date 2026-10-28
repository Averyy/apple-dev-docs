# willBeginMeasuring()

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

A method that XCTest calls when it’s ready to begin running the measured code.

## Declaration

```swift
optional func willBeginMeasuring()
```

```objc
- (void) willBeginMeasuring;
```

## Discussion

XCTest calls this method before it runs a test’s `measure()` or `measure(metrics:)` block. It calls the method once for each iteration of a performance test. Use this method to start gathering measurements.

## See Also

### Recording Metrics
- [func didStopMeasuring()](./didstopmeasuring%28%29.md)
  A method that XCTest calls when it has finished running the measured code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmetric/willbeginmeasuring())*