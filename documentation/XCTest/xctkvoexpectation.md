# XCTKVOExpectation

**Framework**: XCTest  
**Kind**: class

An expectation that a specific key-value observing (KVO) condition fulfills.

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
class XCTKVOExpectation
```

#### Overview

Apple discourages the use of this symbol in Swift. Use [`XCTKeyPathExpectation`](xctkeypathexpectation.md) instead.

## Topics

### Creating KVO expectations
- [convenience init(keyPath: String, object: Any)](xctkvoexpectation/init(keypath:object:).md)
  Creates an expectation that any KVO change to the specified key path of the observed object fulfills.
- [convenience init(keyPath: String, object: Any, expectedValue: Any?)](xctkvoexpectation/init(keypath:object:expectedvalue:).md)
  Creates an expectation a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.
- [init(keyPath: String, object: Any, expectedValue: Any?, options: NSKeyValueObservingOptions)](xctkvoexpectation/init(keypath:object:expectedvalue:options:).md)
  Creates an expectation with custom observation options that a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.
### Expectation properties
- [var keyPath: String](xctkvoexpectation/keypath.md)
  The key path the system observes for KVO changes.
- [var observedObject: Any](xctkvoexpectation/observedobject.md)
  The object that the system observes for KVO changes.
- [var expectedValue: Any?](xctkvoexpectation/expectedvalue.md)
  The value that the key path’s specified property must equal to fulfill the expectation.
- [var options: NSKeyValueObservingOptions](xctkvoexpectation/options.md)
  The key-value observing options the expectation uses when registering for observation.
### Custom KVO evaluation
- [var handler: XCTKVOExpectation.Handler?](xctkvoexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation of changes to the observed key path.
- [XCTKVOExpectation.Handler](xctkvoexpectation/handler-swift.typealias.md)
  A custom handler to call when observing a KVO change for a specified key path.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class XCTKeyPathExpectation](xctkeypathexpectation.md)
  An expectation that a specific key-value observing (KVO) condition fulfills.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation)*