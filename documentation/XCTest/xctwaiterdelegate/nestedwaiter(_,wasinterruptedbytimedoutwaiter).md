# nestedWaiter(_:wasInterruptedByTimedOutWaiter:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Invoked when the waiter is interrupted prior to its expectations being fulfilled or timing out.

## Declaration

```swift
optional func nestedWaiter(_ waiter: XCTWaiter, wasInterruptedByTimedOutWaiter outerWaiter: XCTWaiter)
```

```objc
- (void) nestedWaiter:(XCTWaiter *) waiter wasInterruptedByTimedOutWaiter:(XCTWaiter *) outerWaiter;
```

#### Discussion

This occurs when an “outer” waiter times out, resulting in any waiters nested inside it being interrupted to allow the call stack to quickly unwind.

## See Also

### Timeout Events
- [func waiter(XCTWaiter, didTimeoutWithUnfulfilledExpectations: [XCTestExpectation])](./waiter%28_,didtimeoutwithunfulfilledexpectations%29.md)
  Invoked when not all waited on expectations are fulfilled during the timeout period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiterdelegate/nestedwaiter(_:wasinterruptedbytimedoutwaiter:))*