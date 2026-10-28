# isInverted

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

Indicates that the expectation is not intended to happen.

## Declaration

```swift
var isInverted: Bool { get set }
```

```objc
@property (getter=isInverted) BOOL inverted;
```

## Discussion

To check that a situation does *not* occur during testing, create an expectation that is fulfilled when the unexpected situation occurs, and set its [`isInverted`](./isinverted.md) property to true. Your test will fail immediately if the inverted expectation is fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/isinverted)*