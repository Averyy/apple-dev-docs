# setUp(completion:)

**Framework**: XCTest  
**Kind**: method

Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.

## Declaration

```swift
func setUp() async throws
```

## Mentions

- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)

#### Discussion

> **Note**:  In Swift, `XCTest` does not support overriding this method with a completion handler. Override this method for asynchronous test setup with the following declaration: ```swift
func setUp() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

In Swift, override `setUp() async throws` for asynchronous state preparation with error handling before each test. Do not override `setUp(completion:)` for synchronous state preparation. In Objective-C, override this method for asynchronous state preparation with error handling before each test. Call the completion handler after you have set up your state to notify the test system it can proceed with the next task.

Before each test begins, `XCTest` calls:

1. This method for asynchronous state preparation and error handling,
2. [`setUpWithError()`](xctest/setupwitherror().md) for synchronous state preparation and error handling,
3. Then [`setUp()`](xctest/setup().md) for synchronous state preparation without error handling.

For setup methods that provide error handling, `XCTest` marks the test failed when it catches errors, or skipped when it catches [`XCTSkip`](xctskip-swift.struct.md). Based on your state preparation requirements, choose one of these methods to override in your test case.

## Parameters

- `completion`: In Swift, reserved for system usage. Do not use. In Objective-C, a completion block you must call after you have completed setting up your state asynchronously.

## See Also

- [func setUpWithError() throws](xctest/setupwitherror.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](xctest/setup.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](xctest/teardown(completion:).md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](xctest/teardownwitherror.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.
- [func tearDown()](xctest/teardown.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/setup(completion:))*