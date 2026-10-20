# addTeardownBlock(_:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Registers a block of teardown code to run after the current test method ends.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func addTeardownBlock(_ block: @escaping @MainActor @Sendable () throws -> Void)
```

## Parameters

- `block`: A block of teardown code.

## See Also

### Customizing Test Setup and Teardown
- [Set Up and Tear Down State in Your Tests](../set-up-and-tear-down-state-in-your-tests.md)
  Prepare initial state before tests run, and clean up resources after tests complete.
- [class func setUp()](./setup%28%29.md)
  Provides an opportunity to customize initial state before a test case begins.
- [func addTeardownBlock(() async throws -> Void)](./addteardownblock%28_%29-2guon.md)
  Registers a block of teardown code to run after the current test method ends.
- [class func tearDown()](./teardown%28%29.md)
  Provides an opportunity to perform cleanup after a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/addteardownblock(_:)-5zw6c)*