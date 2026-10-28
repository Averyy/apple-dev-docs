# tearDown()

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to perform cleanup after each test method in a test case ends.

## Declaration

```swift
func tearDown()
```

```objc
- (void) tearDown;
```

## Discussion

After each test completes, `XCTest` calls [`tearDown()`](./teardown%28%29.md), then `tearDownWithError()`, followed by [`tearDown(completion:)`](./teardown%28completion%29.md). Override this method to perform any per-test cleanup.

If state cleanup might throw errors, override [`tearDownWithError()`](./teardownwitherror%28%29.md) or [`tearDown(completion:)`](./teardown%28completion%29.md) instead. `XCTest` marks the test failed when when it catches errors, or skipped when it catches `XCTSkip`.

## See Also

### Related Documentation
- [class func tearDown()](../xctestcase/teardown%28%29.md)
  Provides an opportunity to perform cleanup after a test case ends.
### Setting Up and Tearing Down
- [func setUp(completion: ((any Error)?) -> Void)](./setup%28completion%29.md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUpWithError() throws](./setupwitherror%28%29.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](./setup%28%29.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](./teardown%28completion%29.md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](./teardownwitherror%28%29.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest/teardown())*