# XCTWaiter

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

Waits for the fulfillment of a group of expectations.

## Declaration

```swift
class XCTWaiter
```

```objc
@interface XCTWaiter : NSObject
```

## Overview

You can use waiters with or without a delegate to respond to events such as completion, timeout, or invalid expectation fulfillment. [`XCTestCase`](./xctestcase.md) automatically conforms to the [`XCTWaiterDelegate`](./xctwaiterdelegate.md) protocol and automatically reports timeouts and other unexpected events as test failures.

You can use waiters without a delegate or any association with a test case instance. This allows test support libraries to provide convenience methods for waiting without having to pass test cases through those APIs.

## Topics

### Creating a Waiter
- [init(delegate: (any XCTWaiterDelegate)?)](./xctwaiter/init%28delegate%29.md)
  Creates a new waiter with the specified delegate.
### Waiting for Expectations
- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](./xctwaiter/fulfillment%28of,timeout,enforceorder%29-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](./xctwaiter/wait%28for%29-swift.method.md)
  Waits on a group of expectations.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](./xctwaiter/wait%28for,enforceorder%29-swift.method.md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](./xctwaiter/wait%28for,timeout%29-swift.method.md)
  Waits on a group of expectations for up to the specified timeout.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](./xctwaiter/wait%28for,timeout,enforceorder%29-swift.method.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async -> XCTWaiter.Result](./xctwaiter/fulfillment%28of,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation]) -> XCTWaiter.Result](./xctwaiter/wait%28for%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations.
- [class func wait(for: [XCTestExpectation], enforceOrder: Bool) -> XCTWaiter.Result](./xctwaiter/wait%28for,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations optionally enforcing their order of fulfillment.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval) -> XCTWaiter.Result](./xctwaiter/wait%28for,timeout%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout.
- [class func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) -> XCTWaiter.Result](./xctwaiter/wait%28for,timeout,enforceorder%29-swift.type.method.md)
  Creates a waiter that waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [XCTWaiter.Result](./xctwaiter/result.md)
  Result states returned by a waiter when it completes, times out, fails, or is interrupted.
### Responding to Expectation Fulfilment
- [var delegate: (any XCTWaiterDelegate)?](./xctwaiter/delegate.md)
  The delegate to which expectation fulfillment events will be reported.
- [protocol XCTWaiterDelegate](./xctwaiterdelegate.md)
  Defines methods that are called when [`XCTWaiter`](./xctwaiter.md) expectations are fulfilled correctly or incorrectly.
- [var fulfilledExpectations: [XCTestExpectation]](./xctwaiter/fulfilledexpectations.md)
  An array of expectations that were fulfilled, in order, up until the waiter stopped waiting.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter)*