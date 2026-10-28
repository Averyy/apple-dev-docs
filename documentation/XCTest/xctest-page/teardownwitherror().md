# tearDownWithError()

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.

## Declaration

```swift
func tearDownWithError() throws
```

```objc
- (BOOL) tearDownWithError:(NSError **) error;
```

## Discussion

After each test completes, `XCTest` calls [`tearDown()`](./teardown%28%29.md), then `tearDownWithError()`, followed by [`tearDown(completion:)`](./teardown%28completion%29.md).

If state cleanup might throw errors, override this method or [`tearDown(completion:)`](./teardown%28completion%29.md). `XCTest` marks the test failed when it catches errors, or skipped when it catches `XCTSkip`.

## See Also

### Setting Up and Tearing Down
- [func setUp(completion: ((any Error)?) -> Void)](./setup%28completion%29.md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUpWithError() throws](./setupwitherror%28%29.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](./setup%28%29.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](./teardown%28completion%29.md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDown()](./teardown%28%29.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/teardownwitherror())*