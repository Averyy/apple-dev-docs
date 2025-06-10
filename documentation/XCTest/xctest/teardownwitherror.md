# tearDownWithError()

**Framework**: XCTest  
**Kind**: method

Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.

## Declaration

```swift
func tearDownWithError() throws
```

#### Discussion

After each test completes, `XCTest` calls [`tearDown()`](xctest/teardown().md), then `tearDownWithError()`, followed by [`tearDown(completion:)`](xctest/teardown(completion:).md).

If state cleanup might throw errors, override this method or [`tearDown(completion:)`](xctest/teardown(completion:).md). `XCTest` marks the test failed when it catches errors, or skipped when it catches `XCTSkip`.

## See Also

- [func setUp(completion: ((any Error)?) -> Void)](xctest/setup(completion:).md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUpWithError() throws](xctest/setupwitherror.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](xctest/setup.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](xctest/teardown(completion:).md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDown()](xctest/teardown.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/teardownwitherror())*