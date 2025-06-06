# tearDown()

**Framework**: Xctest  
**Kind**: method

Provides an opportunity to perform cleanup after each test method in a test case ends.

## Declaration

```swift
func tearDown()
```

#### Discussion

After each test completes, `XCTest` calls [`tearDown()`](xctest/teardown().md), then `tearDownWithError()`, followed by [`tearDown(completion:)`](xctest/teardown(completion:).md). Override this method to perform any per-test cleanup.

If state cleanup might throw errors, override [`tearDownWithError()`](xctest/teardownwitherror().md) or [`tearDown(completion:)`](xctest/teardown(completion:).md) instead. `XCTest` marks the test failed when when it catches errors, or skipped when it catches `XCTSkip`.

## See Also

- [class func tearDown()](xctestcase/teardown.md)
  Provides an opportunity to perform cleanup after a test case ends.
- [func setUp(completion: ((any Error)?) -> Void)](xctest/setup(completion:).md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUpWithError() throws](xctest/setupwitherror.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](xctest/setup.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](xctest/teardown(completion:).md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](xctest/teardownwitherror.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/teardown())*