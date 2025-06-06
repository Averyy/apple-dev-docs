# XCTWaiterDelegate

**Framework**: Xctest  
**Kind**: protocol

Defines methods that are called when [`XCTWaiter`](xctwaiter.md) expectations are fulfilled correctly or incorrectly.

## Declaration

```swift
protocol XCTWaiterDelegate : NSObjectProtocol
```

#### Overview

[`XCTestCase`](xctestcase.md) instances automatically conform to the [`XCTWaiterDelegate`](xctwaiterdelegate.md) protocol. If you pass a test case instance as the delegate property of [`XCTWaiter`](xctwaiter.md)’s [`init(delegate:)`](xctwaiter/init(delegate:).md) initializer, that test case will automatically report timeouts and other unexpected events as test failures.

## Topics

### Timeout Events
- [func waiter(XCTWaiter, didTimeoutWithUnfulfilledExpectations: [XCTestExpectation])](xctwaiterdelegate/waiter(_:didtimeoutwithunfulfilledexpectations:).md)
  Invoked when not all waited on expectations are fulfilled during the timeout period.
- [func nestedWaiter(XCTWaiter, wasInterruptedByTimedOutWaiter: XCTWaiter)](xctwaiterdelegate/nestedwaiter(_:wasinterruptedbytimedoutwaiter:).md)
  Invoked when the waiter is interrupted prior to its expectations being fulfilled or timing out.
### Order of Fulfillment Events
- [func waiter(XCTWaiter, fulfillmentDidViolateOrderingConstraintsFor: XCTestExpectation, requiredExpectation: XCTestExpectation)](xctwaiterdelegate/waiter(_:fulfillmentdidviolateorderingconstraintsfor:requiredexpectation:).md)
  Invoked when a waiter is enforcing fulfillment order and an expectation is fulfilled in the wrong order.
### Inverted Expectation Events
- [func waiter(XCTWaiter, didFulfillInvertedExpectation: XCTestExpectation)](xctwaiterdelegate/waiter(_:didfulfillinvertedexpectation:).md)
  Invoked when an expectation whose `isInverted` property is set to `true` is fulfilled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [XCTestCase](xctestcase.md)

## See Also

- [var delegate: (any XCTWaiterDelegate)?](xctwaiter/delegate.md)
  The delegate to which expectation fulfillment events will be reported.
- [var fulfilledExpectations: [XCTestExpectation]](xctwaiter/fulfilledexpectations.md)
  An array of expectations that were fulfilled, in order, up until the waiter stopped waiting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiterdelegate)*