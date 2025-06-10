# waiter(_:didTimeoutWithUnfulfilledExpectations:)

**Framework**: XCTest  
**Kind**: method

Invoked when not all waited on expectations are fulfilled during the timeout period.

## Declaration

```swift
optional func waiter(_ waiter: XCTWaiter, didTimeoutWithUnfulfilledExpectations unfulfilledExpectations: [XCTestExpectation])
```

#### Discussion

If the delegate is an [`XCTestCase`](xctestcase.md) instance, this will be reported as a test failure.

## Parameters

- `waiter`: The   reporting the timeout event.
- `unfulfilledExpectations`: The expectations

## See Also

- [func nestedWaiter(XCTWaiter, wasInterruptedByTimedOutWaiter: XCTWaiter)](xctwaiterdelegate/nestedwaiter(_:wasinterruptedbytimedoutwaiter:).md)
  Invoked when the waiter is interrupted prior to its expectations being fulfilled or timing out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiterdelegate/waiter(_:didtimeoutwithunfulfilledexpectations:))*