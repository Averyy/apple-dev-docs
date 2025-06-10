# nestedWaiter(_:wasInterruptedByTimedOutWaiter:)

**Framework**: XCTest  
**Kind**: method

Invoked when the waiter is interrupted prior to its expectations being fulfilled or timing out.

## Declaration

```swift
optional func nestedWaiter(_ waiter: XCTWaiter, wasInterruptedByTimedOutWaiter outerWaiter: XCTWaiter)
```

#### Discussion

This occurs when an “outer” waiter times out, resulting in any waiters nested inside it being interrupted to allow the call stack to quickly unwind.

## See Also

- [func waiter(XCTWaiter, didTimeoutWithUnfulfilledExpectations: [XCTestExpectation])](xctwaiterdelegate/waiter(_:didtimeoutwithunfulfilledexpectations:).md)
  Invoked when not all waited on expectations are fulfilled during the timeout period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiterdelegate/nestedwaiter(_:wasinterruptedbytimedoutwaiter:))*