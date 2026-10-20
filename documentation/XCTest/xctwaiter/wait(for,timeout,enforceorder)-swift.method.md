# wait(for:timeout:enforceOrder:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.

## Declaration

```swift
func wait(for expectations: [XCTestExpectation], timeout seconds: TimeInterval, enforceOrder enforceOrderOfFulfillment: Bool) -> XCTWaiter.Result
```

```objc
- (XCTWaiterResult) waitForExpectations:(NSArray<XCTestExpectation *> *) expectations timeout:(NSTimeInterval) seconds enforceOrder:(BOOL) enforceOrderOfFulfillment;
```

#### Return Value

A value describing the outcome of waiting for `expectations`.

#### Discussion

Expectations can appear in the `expectations` array only once.

The call may return before the timeout if the test fulfills all the expectations you provide.

In Objective-C code, you might use an expectation to wait on a call to an interface that uses a completion handler to return a result. From Swift code, consider calling `withCheckedContinuation(function:_:)` to use [Concurrency](../../Swift/concurrency.md) instead of an expectation to wait on the result of a completion handler.

## Parameters

- `expectations`: An array of expectations the test must satisfy.
- `seconds`: The time, in seconds, the test allows for the fulfillment of the expectations. The default timeout allows the test to run until it reaches its execution time allowance.
- `enforceOrderOfFulfillment`: If [`true`](../../Swift/true.md), the test must satisfy the expectations in the order they appear in the array.

## See Also

### Waiting for Expectations
- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](./fulfillment%28of,timeout,enforceorder%29-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](./wait%28for%29-swift.method.md)
  Waits on a group of expectations.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,enforceorder%29-swift.method.md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](./wait%28for,timeout%29-swift.method.md)
  Waits on a group of expectations for up to the specified timeout.
- [class func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](./fulfillment%28of,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](./wait%28for%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations.
- [class func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](./wait%28for,timeout%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [XCTWaiter.Result](./result.md)
  Result states returned by a waiter when it completes, times out, fails, or is interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/wait(for:timeout:enforceorder:)-swift.method)*