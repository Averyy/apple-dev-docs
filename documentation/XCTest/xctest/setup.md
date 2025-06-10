# setUp()

**Framework**: XCTest  
**Kind**: method

Provides an opportunity to reset state before calling each test method in a test case.

## Declaration

```swift
func setUp()
```

## Mentions

- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)

#### Discussion

Before each test begins, `XCTest` calls [`setUp(completion:)`](xctest/setup(completion:).md) for asynchronous state preparation, then ``XCTest/XCTest/setUpWithError()```,` followed by this method. Override this method to reset state for each test method.

If state preparation might throw errors, override [`setUp(completion:)`](xctest/setup(completion:).md) or [`setUpWithError()`](xctest/setupwitherror().md) instead.

## See Also

- [class func setUp()](xctestcase/setup.md)
  Provides an opportunity to customize initial state before a test case begins.
- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)
  Prepare initial state before tests run, and clean up resources after tests complete.
- [func setUp(completion: ((any Error)?) -> Void)](xctest/setup(completion:).md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUpWithError() throws](xctest/setupwitherror.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](xctest/teardown(completion:).md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](xctest/teardownwitherror.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.
- [func tearDown()](xctest/teardown.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/setup())*