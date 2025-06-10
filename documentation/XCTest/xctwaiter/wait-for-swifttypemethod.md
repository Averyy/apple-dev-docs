# wait(for:)

**Framework**: XCTest  
**Kind**: method

Creates a waiter that waits on a group of expectations.

## Declaration

```swift
class func wait(for expectations: [XCTestExpectation]) -> XCTWaiter.Result
```

#### Return Value

A value describing the outcome of waiting for `expectations`.

#### Discussion

In Objective-C code, you might use an expectation to wait on a call to an interface that uses a completion handler to return a result. In Swift, consider calling `withCheckedContinuation(function:_:)` to use [`Concurrency`](https://developer.apple.com/documentation/Swift/concurrency) instead of an expectation to wait on the result.

## Parameters

- `expectations`: An array of expectations the test must satisfy.

## See Also

- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](xctwaiter/fulfillment(of:timeout:enforceorder:)-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](xctwaiter/wait(for:)-swift.method.md)
  Waits on a group of expectations.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:enforceorder:)-swift.method.md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:)-swift.method.md)
  Waits on a group of expectations for up to the specified timeout.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:enforceorder:)-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](xctwaiter/fulfillment(of:timeout:enforceorder:)-swift.type.method.md)
  Creates a waiter that waits on group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:enforceorder:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:enforceorder:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [XCTWaiter.Result](xctwaiter/result.md)
  Result states returned by a waiter when it completes, times out, fails, or is interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/wait(for:)-swift.type.method)*