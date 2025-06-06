# waitForExpectations(timeout:handler:)

**Framework**: Xctest  
**Kind**: method

Waits until the test fulfills all expectations or until it times out.

## Declaration

```swift
@MainActor
func waitForExpectations(timeout: TimeInterval, handler: (((any Error)?) -> Void)? = nil)
```

#### Discussion

This method creates a point of synchronization in the flow of a test. Only one [`waitForExpectations(timeout:handler:)`](xctestcase/waitforexpectations(timeout:handler:).md) can be active at any given time, but you can chain together multiple discrete sequences of “create expectations and wait for them to be fulfilled”.

> ❗ **Important**:  This method waits on expectations created with [`XCTestCase`](xctestcase.md)‘s convenience methods only. This method  wait on expectations created manually through initializers on [`XCTestExpectation`](xctestexpectation.md) or its subclasses. To wait for manually created expectations, use the [`wait(for:timeout:)`](xctestcase/wait(for:timeout:).md) or [`wait(for:timeout:enforceOrder:)`](xctestcase/wait(for:timeout:enforceorder:).md) methods, or the corresponding methods on [`XCTWaiter`](xctwaiter.md), passing an explicit list of expectations.

> **Note**:  Clients shouldn’t manipulate the run loop while using this API.

## Parameters

- `timeout`: The time, in seconds, the test allows for the fulfillment of the expectations. The default timeout allows the test to run until it reaches its execution time allowance.
- `handler`: An optional   block to invoke after a test fulfills all expectations or the wait time elapses. A test treats a timeout as a failure.

## See Also

- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async](xctestcase/fulfillment(of:timeout:enforceorder:).md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation])](xctestcase/wait(for:).md)
  Waits on a group of expectations.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool)](xctestcase/wait(for:enforceorder:).md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval)](xctestcase/wait(for:timeout:).md)
  Waits for the test to fulfill a set of expectations within a specified time.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool)](xctestcase/wait(for:timeout:enforceorder:).md)
  Waits for the test to satisfy an array of expectations and specifies whether they must occur in the array’s order.
- [typealias XCWaitCompletionHandler](xcwaitcompletionhandler.md)
  A block the test runner calls when the test fulfills a waiter’s expectations, or when it times out.
- [struct XCTestError](xctesterror.md)
  A type of error that can occur while the test waits to fulfill expectations.
- [XCTestError.Code](xctesterror/code.md)
  Error codes for errors that can occur while the test is waiting to fulfill expectations.
- [let XCTestErrorDomain: String](xctesterrordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/waitforexpectations(timeout:handler:))*