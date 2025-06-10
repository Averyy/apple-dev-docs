# tearDown()

**Framework**: XCTest  
**Kind**: method

Provides an opportunity to perform cleanup after a test case ends.

## Declaration

```swift
class func tearDown()
```

## Mentions

- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)

#### Discussion

The [`tearDown()`](xctestcase/teardown().md) class method is called exactly once for a test case, after its final test method completes. Override this method to perform any cleanup after all test methods have ended.

## See Also

- [func tearDown()](xctest/teardown.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.
- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)
  Prepare initial state before tests run, and clean up resources after tests complete.
- [class func setUp()](xctestcase/setup.md)
  Provides an opportunity to customize initial state before a test case begins.
- [func addTeardownBlock(() async throws -> Void)](xctestcase/addteardownblock(_:)-2guon.md)
  Registers a block of teardown code to run after the current test method ends.
- [func addTeardownBlock(() throws -> Void)](xctestcase/addteardownblock(_:)-5zw6c.md)
  Registers a block of teardown code to run after the current test method ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/teardown())*