# setUp(completion:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.

## Declaration

```swift
func setUp(completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setUp() async throws
```

```objc
- (void) setUpWithCompletionHandler:(void (^)(NSError *error)) completion;
```

## Mentions

- [Set Up and Tear Down State in Your Tests](../set-up-and-tear-down-state-in-your-tests.md)

## Discussion

In Swift, override `setUp() async throws` for asynchronous state preparation with error handling before each test. Do not override `setUp(completion:)` for synchronous state preparation. In Objective-C, override this method for asynchronous state preparation with error handling before each test. Call the completion handler after you have set up your state to notify the test system it can proceed with the next task.

Before each test begins, `XCTest` calls:

1. This method for asynchronous state preparation and error handling,
2. [`setUpWithError()`](./setupwitherror%28%29.md) for synchronous state preparation and error handling,
3. Then [`setUp()`](./setup%28%29.md) for synchronous state preparation without error handling.

For setup methods that provide error handling, `XCTest` marks the test failed when it catches errors, or skipped when it catches [`XCTSkip`](../xctskip-swift.struct.md). Based on your state preparation requirements, choose one of these methods to override in your test case.

## Parameters

- `completion`: In Swift, reserved for system usage. Do not use. In Objective-C, a completion block you must call after you have completed setting up your state asynchronously.

## See Also

### Setting Up and Tearing Down
- [func setUpWithError() throws](./setupwitherror%28%29.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](./setup%28%29.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](./teardown%28completion%29.md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](./teardownwitherror%28%29.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.
- [func tearDown()](./teardown%28%29.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/setup(completion:))*