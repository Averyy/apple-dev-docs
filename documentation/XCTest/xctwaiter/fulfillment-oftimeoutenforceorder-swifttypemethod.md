# fulfillment(of:timeout:enforceOrder:)

**Framework**: Xctest  
**Kind**: method

Creates a waiter that waits on group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@nonobjc
class func fulfillment(of expectations: [XCTestExpectation], timeout seconds: TimeInterval = .infinity, enforceOrder enforceOrderOfFulfillment: Bool = false) async -> XCTWaiter.Result
```

#### Return Value

A value describing the outcome of waiting for `expectations`.

#### Discussion

Use this Concurrency safe alternative to [`wait(for:timeout:enforceOrder:)`](xctwaiter/wait(for:timeout:enforceorder:)-swift.type.method.md) in your Swift code. A call to [`wait(for:timeout:enforceOrder:)`](xctwaiter/wait(for:timeout:enforceorder:)-swift.type.method.md) runs synchronously and blocks the calling thread, which can cause deadlocks or priority inversion.

Expectations can only appear in the array once. The call may return before the timeout if the test fulfills all the expectations you provide.

> **Note**:  If you don’t specify a timeout when calling this function, enable test timeouts to prevent unfulfilled expectation from hanging the test.

 If you don’t specify a timeout when calling this function, enable test timeouts to prevent unfulfilled expectation from hanging the test.

The test discards the waiter after the wait completes.

## Parameters

- `expectations`: An array of expectations the test must satisfy.
- `seconds`: The time, in seconds, the test allows for the fulfillment of the expectations.
- `enforceOrderOfFulfillment`: If  , the test must satisfy the expectations in the order they appear in the array.

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
- [class func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](xctwaiter/wait(for:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations.
- [class func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:enforceorder:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](xctwaiter/wait(for:timeout:enforceorder:)-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [XCTWaiter.Result](xctwaiter/result.md)
  Result states returned by a waiter when it completes, times out, fails, or is interrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/fulfillment(of:timeout:enforceorder:)-swift.type.method)*