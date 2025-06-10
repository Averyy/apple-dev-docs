# XCTNSPredicateExpectation.Handler

**Framework**: XCTest  
**Kind**: typealias

A handler XCTest calls when evaluating the predicate returns `true`.

## Declaration

```swift
typealias Handler = () -> Bool
```

#### Return Value

Your custom handler should return [`true`](https://developer.apple.com/documentation/swift/true) if the expectation is considered fulfilled, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var handler: XCTNSPredicateExpectation.Handler?](xctnspredicateexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation when `predicate` evaluates as `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnspredicateexpectation/handler-swift.typealias)*