# handler

**Framework**: Xctest  
**Kind**: property

An optional handler that performs custom evaluation when `predicate` evaluates as `true`.

## Declaration

```swift
var handler: XCTNSPredicateExpectation.Handler? { get set }
```

#### Discussion

If a handler isn’t provided, the first successful evaluation of the predicate fulfills the expectation. If you provide a handler, the handler can override this default behavior to tailor the conditions that fulfill the expectation.

## See Also

- [XCTNSPredicateExpectation.Handler](xctnspredicateexpectation/handler-swift.typealias.md)
  A handler XCTest calls when evaluating the predicate returns `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnspredicateexpectation/handler-swift.property)*