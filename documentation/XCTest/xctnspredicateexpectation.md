# XCTNSPredicateExpectation

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An expectation that’s fulfilled when an `NSPredicate` is satisfied.

## Declaration

```swift
class XCTNSPredicateExpectation
```

```objc
@interface XCTNSPredicateExpectation : XCTestExpectation
```

## Overview

When you use an instance of this class from Swift and await using [`fulfillment(of:timeout:enforceOrder:)`](./xctestcase/fulfillment%28of,timeout,enforceorder%29.md) rather than [`wait(for:)`](./xctestcase/wait%28for%29.md), XCTest evaluates the associated predicate on the main actor.

## Topics

### Creating a Predicate-Based Expectation
- [init(predicate: NSPredicate, object: Any?)](./xctnspredicateexpectation/init%28predicate,object%29.md)
  Creates an expectation that’s fulfilled when an `NSPredicate` instance returns `true`, optionally for a provided object.
### Expectation Properties
- [var predicate: NSPredicate](./xctnspredicateexpectation/predicate.md)
  The predicate the expectation evaluates.
- [var object: Any?](./xctnspredicateexpectation/object.md)
  An optional object against which the predicate evaluates.
### Handling Predicate Resolution
- [var handler: XCTNSPredicateExpectation.Handler?](./xctnspredicateexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation when `predicate` evaluates as `true`.
- [XCTNSPredicateExpectation.Handler](./xctnspredicateexpectation/handler-swift.typealias.md)
  A handler XCTest calls when evaluating the predicate returns `true`.

## Relationships

### Inherits From
- [XCTestExpectation](./xctestexpectation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnspredicateexpectation)*