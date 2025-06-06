# Preventing memory-use regressions

**Framework**: Xcode

Measure the memory that your app’s features use, and detect increases by using XCTest performance tests.

#### Overview

[`XCTest`](https://developer.apple.com/documentation/XCTest) can measure the amount of memory allocated by your app while it executes a test case. To measure memory use, create a performance test in your app’s unit test target, and pass an instance of [`XCTMemoryMetric`](https://developer.apple.com/documentation/XCTest/XCTMemoryMetric) to `measure(metrics:)`. Inside the block, call the code from your app that demonstrates the problematic memory use.

```swift
class MemoryTests: XCTestCase {
    func testMemoryUse() {
        self.measure(metrics: [XCTMemoryMetric()]) {
          // Use the relevant app feature here
        }
    }
}
```

When you run this test, Xcode measures the peak memory use observed while the block runs, and the growth in memory allocated between the block’s beginning and end. You can observe these values by clicking the icon next to the test results. Click Set Baseline to establish a value for future comparisons. The test fails if the memory use significantly exceeds the baseline measurement.

## See Also

- [Gathering information about memory use](gathering-information-about-memory-use.md)
  Identify memory-use inefficiencies by measuring and profiling your app.
- [Making changes to reduce memory use](making-changes-to-reduce-memory-use.md)
  Decrease your app’s use of memory by addressing common causes of excessive use.
- [Responding to low-memory warnings](responding-to-low-memory-warnings.md)
  Detect when your app is using excessive memory, and bring memory use under control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/preventing-memory-use-regressions)*