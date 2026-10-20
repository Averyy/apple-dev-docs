# XCTWaiter.Result

**Framework**: XCTest  
**Kind**: enum  
**Role**: Enumeration

Result states returned by a waiter when it completes, times out, fails, or is interrupted.

## Declaration

```swift
enum Result
```

```c
enum XCTWaiterResult : NSInteger;
```

## Topics

### Result States
- [XCTWaiter.Result.completed](./result/completed.md)
  All of the waiter’s expectations were fulfilled successfully.
- [XCTWaiter.Result.timedOut](./result/timedout.md)
  The waiter timed out before all of its expectations were fulfilled.
- [XCTWaiter.Result.incorrectOrder](./result/incorrectorder.md)
  The waiter’s expectations were not fulfilled in the required order.
- [XCTWaiter.Result.invertedFulfillment](./result/invertedfulfillment.md)
  An inverted expectation was fulfilled.
- [XCTWaiter.Result.interrupted](./result/interrupted.md)
  The waiter was interrupted prior to its expectations being fulfilled or timing out.
### Initializers
- [init?(rawValue: Int)](./result/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](./wait%28for,timeout%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](./wait%28for,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/result)*