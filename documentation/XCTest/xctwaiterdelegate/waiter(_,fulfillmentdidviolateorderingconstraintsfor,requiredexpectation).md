# waiter(_:fulfillmentDidViolateOrderingConstraintsFor:requiredExpectation:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Invoked when a waiter is enforcing fulfillment order and an expectation is fulfilled in the wrong order.

## Declaration

```swift
optional func waiter(_ waiter: XCTWaiter, fulfillmentDidViolateOrderingConstraintsFor expectation: XCTestExpectation, requiredExpectation: XCTestExpectation)
```

```objc
- (void) waiter:(XCTWaiter *) waiter fulfillmentDidViolateOrderingConstraintsForExpectation:(XCTestExpectation *) expectation requiredExpectation:(XCTestExpectation *) requiredExpectation;
```

#### Discussion

If the delegate is an [`XCTestCase`](../xctestcase.md) instance, this will be reported as a test failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiterdelegate/waiter(_:fulfillmentdidviolateorderingconstraintsfor:requiredexpectation:))*