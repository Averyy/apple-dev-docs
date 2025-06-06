# XCTKeyPathExpectation

**Framework**: Xctest  
**Kind**: class

An expectation that a specific key-value observing (KVO) condition fulfills.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

## Declaration

```swift
final class XCTKeyPathExpectation<T, V> where T : NSObject
```

#### Overview

Use an instance of this class to asynchronously wait for changes to a property you specify by key path for a given object. When the value of the property changes, the expectation compares the new value using a predicate or expected value you provide.

## Topics

### Creating key path expectations
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, expectedValue: V)](xctkeypathexpectation/init(keypath:observedobject:options:expectedvalue:).md)
  Creates an expectation that the system fulfills when the value of the observed property changes to an expected value.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, predicate: XCTKeyPathExpectation<T, V>.Predicate?)](xctkeypathexpectation/init(keypath:observedobject:options:predicate:).md)
  Creates an expectation that the system fulfills when the value of the observed property changes and satisfies the conditions of a predicate’s evaluation.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.SynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-plka.md)
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.AsynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-8noag.md)
- [XCTKeyPathExpectation.AsynchronousFilter](xctkeypathexpectation/asynchronousfilter.md)
- [XCTKeyPathExpectation.SynchronousFilter](xctkeypathexpectation/synchronousfilter.md)
- [XCTKeyPathExpectation.Predicate](xctkeypathexpectation/predicate.md)
  A function the key path expectation uses to test the value of an observed property.
### Expectation properties
- [let keyPath: KeyPath<T, V>](xctkeypathexpectation/keypath.md)
  The key path for the observed property, relative to the observed object.
- [let observedObject: T](xctkeypathexpectation/observedobject.md)
  The object the system observes the key path on.
- [let options: NSKeyValueObservingOptions](xctkeypathexpectation/options.md)
  A combination of values that specify what to include in observation notifications.
- [var expectedValue: V?](xctkeypathexpectation/expectedvalue.md)
  A value that the key path’s specified property must equal to fulfill the expectation.

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

## See Also

- [Using Key-Value Observing in Swift](../Swift/using-key-value-observing-in-swift.md)
  Notify objects about changes to the properties of other objects.
- [class XCTKVOExpectation](xctkvoexpectation.md)
  An expectation that a specific key-value observing (KVO) condition fulfills.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation)*