# handler

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

An optional handler that performs custom evaluation of changes to the observed key path.

**Availability**:
- iOS - Deprecated in 17.0
- iPadOS - Deprecated in 17.0
- Mac Catalyst - Deprecated in 17.0
- macOS - Deprecated in 27.0
- tvOS - Deprecated in 17.0
- visionOS - Deprecated in 1.0
- watchOS - Deprecated in 26.0

> **Deprecated**: Replaced by 'XCTKeyPathExpectation'

## Declaration

```swift
var handler: XCTKVOExpectation.Handler? { get set }
```

```objc
@property (atomic, copy, nullable) XCKeyValueObservingExpectationHandler handler;
```

## Discussion

> **Note**:  The system ignores the expectation’s [`expectedValue`](./expectedvalue.md) property when the [`handler`](./handler-swift.property.md) is non-nil.

## See Also

### Custom KVO evaluation
- [XCTKVOExpectation.Handler](./handler-swift.typealias.md)
  A custom handler to call when observing a KVO change for a specified key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/handler-swift.property)*