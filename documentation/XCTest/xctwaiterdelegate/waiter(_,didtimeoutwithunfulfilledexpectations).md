# waiter(_:didTimeoutWithUnfulfilledExpectations:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Invoked when not all waited on expectations are fulfilled during the timeout period.

## Declaration

```swift
optional func waiter(_ waiter: XCTWaiter, didTimeoutWithUnfulfilledExpectations unfulfilledExpectations: [XCTestExpectation])
```

```objc
- (void) waiter:(XCTWaiter *) waiter didTimeoutWithUnfulfilledExpectations:(NSArray<XCTestExpectation *> *) unfulfilledExpectations;
```

## Discussion

If the delegate is an [`XCTestCase`](../xctestcase.md) instance, this will be reported as a test failure.

## Parameters

- `waiter`: The [`XCTWaiter`](../xctwaiter.md) reporting the timeout event.
- `unfulfilledExpectations`: The expectations

## See Also

### Timeout Events
- [func nestedWaiter(XCTWaiter, wasInterruptedByTimedOutWaiter: XCTWaiter)](./nestedwaiter%28_,wasinterruptedbytimedoutwaiter%29.md)
  Invoked when the waiter is interrupted prior to its expectations being fulfilled or timing out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiterdelegate/waiter(_:didtimeoutwithunfulfilledexpectations:))*