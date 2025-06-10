# setUp()

**Framework**: XCTest  
**Kind**: method

Provides an opportunity to customize initial state before a test case begins.

## Declaration

```swift
class func setUp()
```

## Mentions

- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)

#### Discussion

The [`setUp()`](xctestcase/setup().md) class method is called exactly once for a test case, before its first test method is called. Override this method to customize the initial state for all tests in the test case.

## See Also

- [func setUp()](xctest/setup.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)
  Prepare initial state before tests run, and clean up resources after tests complete.
- [func addTeardownBlock(() async throws -> Void)](xctestcase/addteardownblock(_:)-2guon.md)
  Registers a block of teardown code to run after the current test method ends.
- [func addTeardownBlock(() throws -> Void)](xctestcase/addteardownblock(_:)-5zw6c.md)
  Registers a block of teardown code to run after the current test method ends.
- [class func tearDown()](xctestcase/teardown.md)
  Provides an opportunity to perform cleanup after a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/setup())*