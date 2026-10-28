# wait(for:timeout:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Type Method

Creates a waiter that waits on a group of expectations for up to the specified timeout.

## Declaration

```swift
class func wait(for expectations: [XCTestExpectation], timeout seconds: TimeInterval) -> XCTWaiter.Result
```

```objc
+ (XCTWaiterResult) waitForExpectations:(NSArray<XCTestExpectation *> *) expectations timeout:(NSTimeInterval) seconds;
```

## Return Value

A value describing the outcome of waiting for `expectations`.

## Discussion

Expectations can only appear in the array once. The test discards the waiter when the wait completes.

In Objective-C code, you might use an expectation to wait on a call to an interface that uses a completion handler to return a result. From Swift code, consider calling `withCheckedContinuation(function:_:)` to use [Concurrency](../../Swift/concurrency.md) instead of an expectation to wait on the result of a completion handler.

## Parameters

- `expectations`: An array of expectations the test must satisfy.
- `seconds`: The time, in seconds, the test allows for the fulfillment of the expectations. The default timeout allows the test to run until it reaches its execution time allowance.

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
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,timeout,enforceorder%29-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](./fulfillment%28of,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](./wait%28for%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations.
- [class func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [XCTWaiter.Result](./result.md)
  Result states returned by a waiter when it completes, times out, fails, or is interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/wait(for:timeout:)-swift.type.method)*