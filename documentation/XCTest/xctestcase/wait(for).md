# wait(for:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Waits on a group of expectations.

## Declaration

```swift
func wait(for expectations: [XCTestExpectation])
```

```objc
- (void) waitForExpectations:(NSArray<XCTestExpectation *> *) expectations;
```

## Discussion

> **Note**:  Use [`fulfillment(of:timeout:enforceOrder:)`](./fulfillment%28of,timeout,enforceorder%29.md) in Swift code requiring concurrency.

In Objective-C code, you might use an expectation to wait on a call to an interface that uses a completion handler to return a result. From Swift code, consider calling `withCheckedContinuation(function:_:)` to use [Concurrency](../../Swift/concurrency.md) instead of an expectation to wait on the result of a completion handler.

## Parameters

- `expectations`: An array of expectations the test must satisfy.

## See Also

### Waiting for Expectations
- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async](./fulfillment%28of,timeout,enforceorder%29.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool)](./wait%28for,enforceorder%29.md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval)](./wait%28for,timeout%29.md)
  Waits for the test to fulfill a set of expectations within a specified time.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool)](./wait%28for,timeout,enforceorder%29.md)
  Waits for the test to satisfy an array of expectations and specifies whether they must occur in the array’s order.
- [func waitForExpectations(timeout: TimeInterval, handler: (((any Error)?) -> Void)?)](./waitforexpectations%28timeout,handler%29.md)
  Waits until the test fulfills all expectations or until it times out.
- [typealias XCWaitCompletionHandler](../xcwaitcompletionhandler.md)
  A block the test runner calls when the test fulfills a waiter’s expectations, or when it times out.
- [struct XCTestError](../xctesterror.md)
  A type of error that can occur while the test waits to fulfill expectations.
- [XCTestError.Code](../xctesterror/code.md)
  Error codes for errors that can occur while the test is waiting to fulfill expectations.
- [let XCTestErrorDomain: String](../xctesterrordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/wait(for:))*