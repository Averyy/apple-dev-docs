# XCTestError

**Framework**: XCTest  
**Kind**: struct  
**Role**: Structure

A type of error that can occur while the test waits to fulfill expectations.

## Declaration

```swift
struct XCTestError
```

## Topics

### Classifying Errors with Codes
- [static var timeoutWhileWaiting: XCTestError.Code](./xctesterror/timeoutwhilewaiting.md)
  A code that represents a timeout the test encountered while waiting to fulfill expectations.
- [static var failureWhileWaiting: XCTestError.Code](./xctesterror/failurewhilewaiting.md)
  A code that represents a test failure the test encountered while waiting to fulfill expectations.
- [XCTestError.Code](./xctesterror/code.md)
  Error codes for errors that can occur while the test is waiting to fulfill expectations.
### Classifying Errors by Domain
- [let XCTestErrorDomain: String](./xctesterrordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.
### Type Properties
- [static var errorDomain: String](./xctesterror/errordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Waiting for Expectations
- [func fulfillment(of: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool) async](./xctestcase/fulfillment%28of,timeout,enforceorder%29.md)
  Waits on a group of expectations for up to the specified timeout, optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation])](./xctestcase/wait%28for%29.md)
  Waits on a group of expectations.
- [func wait(for: [XCTestExpectation], enforceOrder: Bool)](./xctestcase/wait%28for,enforceorder%29.md)
  Waits on a group of expectations optionally enforcing their order of fulfillment.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval)](./xctestcase/wait%28for,timeout%29.md)
  Waits for the test to fulfill a set of expectations within a specified time.
- [func wait(for: [XCTestExpectation], timeout: TimeInterval, enforceOrder: Bool)](./xctestcase/wait%28for,timeout,enforceorder%29.md)
  Waits for the test to satisfy an array of expectations and specifies whether they must occur in the array’s order.
- [func waitForExpectations(timeout: TimeInterval, handler: (((any Error)?) -> Void)?)](./xctestcase/waitforexpectations%28timeout,handler%29.md)
  Waits until the test fulfills all expectations or until it times out.
- [typealias XCWaitCompletionHandler](./xcwaitcompletionhandler.md)
  A block the test runner calls when the test fulfills a waiter’s expectations, or when it times out.
- [XCTestError.Code](./xctesterror/code.md)
  Error codes for errors that can occur while the test is waiting to fulfill expectations.
- [let XCTestErrorDomain: String](./xctesterrordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctesterror)*