# XCTNSPredicateExpectation.Handler

**Framework**: XCTest  
**Kind**: typealias  
**Role**: Type Alias

A handler XCTest calls when evaluating the predicate returns `true`.

## Declaration

```swift
typealias Handler = @Sendable () -> Bool
```

```c
typedef _Bool (^)(void) XCPredicateExpectationHandler;
```

## Return Value

Your custom handler should return [`true`](../../Swift/true.md) if the expectation is considered fulfilled, otherwise [`false`](../../Swift/false.md).

## See Also

### Handling Predicate Resolution
- [var handler: XCTNSPredicateExpectation.Handler?](./handler-swift.property.md)
  An optional handler that performs custom evaluation when `predicate` evaluates as `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnspredicateexpectation/handler-swift.typealias)*