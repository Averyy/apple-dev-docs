# XCTNSPredicateExpectation

**Framework**: Xctest  
**Kind**: class

An expectation that’s fulfilled when an `NSPredicate` is satisfied.

## Declaration

```swift
class XCTNSPredicateExpectation
```

#### Overview

When you use an instance of this class from Swift and await using [`fulfillment(of:timeout:enforceOrder:)`](xctestcase/fulfillment(of:timeout:enforceorder:).md) rather than [`wait(for:)`](xctestcase/wait(for:).md), XCTest evaluates the associated predicate on the main actor.

## Topics

### Creating a Predicate-Based Expectation
- [init(predicate: NSPredicate, object: Any?)](xctnspredicateexpectation/init(predicate:object:).md)
  Creates an expectation that’s fulfilled when an `NSPredicate` instance returns `true`, optionally for a provided object.
### Expectation Properties
- [var predicate: NSPredicate](xctnspredicateexpectation/predicate.md)
  The predicate the expectation evaluates.
- [var object: Any?](xctnspredicateexpectation/object.md)
  An optional object against which the predicate evaluates.
### Handling Predicate Resolution
- [var handler: XCTNSPredicateExpectation.Handler?](xctnspredicateexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation when `predicate` evaluates as `true`.
- [XCTNSPredicateExpectation.Handler](xctnspredicateexpectation/handler-swift.typealias.md)
  A handler XCTest calls when evaluating the predicate returns `true`.

## Relationships

### Inherits From
- [XCTestExpectation](xctestexpectation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnspredicateexpectation)*