# setUpWithError()

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to reset state and to throw errors before calling each test method in a test case.

## Declaration

```swift
func setUpWithError() throws
```

```objc
- (BOOL) setUpWithError:(NSError **) error;
```

## Mentions

- [Set Up and Tear Down State in Your Tests](../set-up-and-tear-down-state-in-your-tests.md)

#### Discussion

Before each test begins, `XCTest` calls [`setUp(completion:)`](./setup%28completion%29.md) for asynchronous state preparation, then this method, followed by [`setUp()`](./setup%28%29.md).

If state preparation might throw errors, override [`setUp(completion:)`](./setup%28completion%29.md) or this method. `XCTest` marks the test failed when it catches errors, or skipped when it catches `XCTSkip`.

## See Also

### Setting Up and Tearing Down
- [func setUp(completion: ((any Error)?) -> Void)](./setup%28completion%29.md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUp()](./setup%28%29.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](./teardown%28completion%29.md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](./teardownwitherror%28%29.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.
- [func tearDown()](./teardown%28%29.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/setupwitherror())*