# waiter(_:didFulfillInvertedExpectation:)

**Framework**: Xctest  
**Kind**: method

Invoked when an expectation whose `isInverted` property is set to `true` is fulfilled.

## Declaration

```swift
optional func waiter(_ waiter: XCTWaiter, didFulfillInvertedExpectation expectation: XCTestExpectation)
```

#### Discussion

If the delegate is an [`XCTestCase`](xctestcase.md) instance, this will be reported as a test failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiterdelegate/waiter(_:didfulfillinvertedexpectation:))*