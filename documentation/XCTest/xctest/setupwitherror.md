# setUpWithError()

**Framework**: XCTest  
**Kind**: method

Provides an opportunity to reset state and to throw errors before calling each test method in a test case.

## Declaration

```swift
func setUpWithError() throws
```

## Mentions

- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)

#### Discussion

Before each test begins, `XCTest` calls [`setUp(completion:)`](xctest/setup(completion:).md) for asynchronous state preparation, then this method, followed by [`setUp()`](xctest/setup().md).

If state preparation might throw errors, override [`setUp(completion:)`](xctest/setup(completion:).md) or this method. `XCTest` marks the test failed when it catches errors, or skipped when it catches `XCTSkip`.

## See Also

- [func setUp(completion: ((any Error)?) -> Void)](xctest/setup(completion:).md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUp()](xctest/setup.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](xctest/teardown(completion:).md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](xctest/teardownwitherror.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.
- [func tearDown()](xctest/teardown.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/setupwitherror())*