# isInverted

**Framework**: XCTest  
**Kind**: property

Indicates that the expectation is not intended to happen.

## Declaration

```swift
var isInverted: Bool { get set }
```

#### Discussion

To check that a situation does  occur during testing, create an expectation that is fulfilled when the unexpected situation occurs, and set its [`isInverted`](xctestexpectation/isinverted.md) property to true. Your test will fail immediately if the inverted expectation is fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/isinverted)*