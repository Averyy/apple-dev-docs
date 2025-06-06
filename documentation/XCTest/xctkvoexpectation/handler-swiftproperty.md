# handler

**Framework**: Xctest  
**Kind**: property

An optional handler that performs custom evaluation of changes to the observed key path.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var handler: XCTKVOExpectation.Handler? { get set }
```

#### Discussion

> **Note**:  The system ignores the expectation’s [`expectedValue`](xctkvoexpectation/expectedvalue.md) property when the [`handler`](xctkvoexpectation/handler-swift.property.md) is non-nil.

 The system ignores the expectation’s [`expectedValue`](xctkvoexpectation/expectedvalue.md) property when the [`handler`](xctkvoexpectation/handler-swift.property.md) is non-nil.

## See Also

- [XCTKVOExpectation.Handler](xctkvoexpectation/handler-swift.typealias.md)
  A custom handler to call when observing a KVO change for a specified key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation/handler-swift.property)*