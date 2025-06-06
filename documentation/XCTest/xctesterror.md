# XCTestError

**Framework**: Xctest  
**Kind**: struct

A type of error that can occur while the test waits to fulfill expectations.

## Declaration

```swift
struct XCTestError
```

## Topics

### Classifying Errors with Codes
- [static var timeoutWhileWaiting: XCTestError.Code](xctesterror/timeoutwhilewaiting.md)
  A code that represents a timeout the test encountered while waiting to fulfill expectations.
- [static var failureWhileWaiting: XCTestError.Code](xctesterror/failurewhilewaiting.md)
  A code that represents a test failure the test encountered while waiting to fulfill expectations.
- [XCTestError.Code](xctesterror/code.md)
  Error codes for errors that can occur while the test is waiting to fulfill expectations.
### Classifying Errors by Domain
- [let XCTestErrorDomain: String](xctesterrordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.
### Type Properties
- [static var errorDomain: String](xctesterror/errordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

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
- [func waitForExpectations(timeout: TimeInterval, handler: (((any Error)?) -> Void)?)](xctestcase/waitforexpectations(timeout:handler:).md)
  Waits until the test fulfills all expectations or until it times out.
- [typealias XCWaitCompletionHandler](xcwaitcompletionhandler.md)
  A block the test runner calls when the test fulfills a waiter’s expectations, or when it times out.
- [XCTestError.Code](xctesterror/code.md)
  Error codes for errors that can occur while the test is waiting to fulfill expectations.
- [let XCTestErrorDomain: String](xctesterrordomain.md)
  The error domain for errors that can occur while the test is waiting to fulfill expectations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctesterror)*