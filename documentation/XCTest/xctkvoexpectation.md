# XCTKVOExpectation

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An expectation that a specific key-value observing (KVO) condition fulfills.

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
class XCTKVOExpectation
```

```objc
@interface XCTKVOExpectation : XCTestExpectation
```

## Overview

Apple discourages the use of this symbol in Swift. Use [`XCTKeyPathExpectation`](./xctkeypathexpectation.md) instead.

## Topics

### Creating KVO expectations
- [convenience init(keyPath: String, object: Any)](./xctkvoexpectation/init%28keypath,object%29.md)
  Creates an expectation that any KVO change to the specified key path of the observed object fulfills.
- [convenience init(keyPath: String, object: Any, expectedValue: Any?)](./xctkvoexpectation/init%28keypath,object,expectedvalue%29.md)
  Creates an expectation a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.
- [init(keyPath: String, object: Any, expectedValue: Any?, options: NSKeyValueObservingOptions)](./xctkvoexpectation/init%28keypath,object,expectedvalue,options%29.md)
  Creates an expectation with custom observation options that a KVO change fulfills when it causes the specified key path of the observed object to have an expected value.
### Expectation properties
- [var keyPath: String](./xctkvoexpectation/keypath.md)
  The key path the system observes for KVO changes.
- [var observedObject: Any](./xctkvoexpectation/observedobject.md)
  The object that the system observes for KVO changes.
- [var expectedValue: Any?](./xctkvoexpectation/expectedvalue.md)
  The value that the key path’s specified property must equal to fulfill the expectation.
- [var options: NSKeyValueObservingOptions](./xctkvoexpectation/options.md)
  The key-value observing options the expectation uses when registering for observation.
### Custom KVO evaluation
- [var handler: XCTKVOExpectation.Handler?](./xctkvoexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation of changes to the observed key path.
- [XCTKVOExpectation.Handler](./xctkvoexpectation/handler-swift.typealias.md)
  A custom handler to call when observing a KVO change for a specified key path.

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

## See Also

### Key Value Observing Expectations
- [class XCTKeyPathExpectation](./xctkeypathexpectation.md)
  An expectation that a specific key-value observing (KVO) condition fulfills.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkvoexpectation)*