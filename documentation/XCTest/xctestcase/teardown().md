# tearDown()

**Framework**: XCTest  
**Kind**: method  
**Role**: Type Method

Provides an opportunity to perform cleanup after a test case ends.

## Declaration

```swift
class func tearDown()
```

```objc
+ (void) tearDown;
```

## Mentions

- [Set Up and Tear Down State in Your Tests](../set-up-and-tear-down-state-in-your-tests.md)

## Discussion

The [`tearDown()`](./teardown%28%29.md) class method is called exactly once for a test case, after its final test method completes. Override this method to perform any cleanup after all test methods have ended.

## See Also

### Related Documentation
- [func tearDown()](../xctest-page/teardown%28%29.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.
### Customizing Test Setup and Teardown
- [Set Up and Tear Down State in Your Tests](../set-up-and-tear-down-state-in-your-tests.md)
  Prepare initial state before tests run, and clean up resources after tests complete.
- [class func setUp()](./setup%28%29.md)
  Provides an opportunity to customize initial state before a test case begins.
- [func addTeardownBlock(() async throws -> Void)](./addteardownblock%28_%29-2guon.md)
  Registers a block of teardown code to run after the current test method ends.
- [func addTeardownBlock(() throws -> Void)](./addteardownblock%28_%29-5zw6c.md)
  Registers a block of teardown code to run after the current test method ends.
- [- addAsyncTeardownBlock:](./addasyncteardownblock_.md)
  Registers a block of asynchronous teardown code to run after the current test method ends.
- [- addTeardownBlock:](./addteardownblock_.md)
  Registers a block of teardown code to run after the current test method ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/teardown())*