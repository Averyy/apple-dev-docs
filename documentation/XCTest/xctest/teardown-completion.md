# tearDown(completion:)

**Framework**: XCTest  
**Kind**: method

Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.

## Declaration

```swift
func tearDown() async throws
```

#### Discussion

> **Note**:  In Swift, `XCTest` does not support overriding this method with a completion handler. Override this method for asynchronous test tear down with the following declaration: ```swift
func tearDown() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

In Swift, override `tearDown() async throws` for asynchronous state cleanup with error handling after each test. Do not override `tearDown(completion:)` for synchronous state cleanup.

In Objective-C, override this method for asynchronous state cleanup with error handling after each test. Call the completion handler after you have cleaned up your state to notify the test system it can proceed with the next task.

After each test completes, `XCTest` calls:

1. [`tearDown()`](xctest/teardown().md) for synchronous state cleanup without error handling,
2. [`tearDownWithError()`](xctest/teardownwitherror().md) for synchronous state cleanup and error handling,
3. Then this method for asynchronous state preparation and error handling.

For tear down methods that provide error handling, `XCTest` marks the test failed when it catches errors, or skipped when it catches [`XCTSkip`](xctskip-swift.struct.md). Based on your state cleanup requirements, choose one of these methods to override in your test case.

## Parameters

- `completion`: In Swift, reserved for system usage. Do not use. In Objective-C, a completion block you must call after you have completed cleaning up your state asynchronously.

## See Also

- [func setUp(completion: ((any Error)?) -> Void)](xctest/setup(completion:).md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUpWithError() throws](xctest/setupwitherror.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](xctest/setup.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDownWithError() throws](xctest/teardownwitherror.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.
- [func tearDown()](xctest/teardown.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/teardown(completion:))*