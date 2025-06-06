# init(keyPath:observedObject:options:expectedValue:)

**Framework**: Xctest  
**Kind**: init

Creates an expectation that the system fulfills when the value of the observed property changes to an expected value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

## Declaration

```swift
convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions = [.initial, .new, .old], expectedValue: V)
```

#### Discussion

Use this initializer to create an expectation that observes changes on the observed object until the value of the property matches the expected value, fulfilling the expectation.

## Parameters

- `keyPath`: The key path for the observed property, relative to the observed object.
- `observedObject`: The object to observe the key path on.
- `options`: A combination of values that specify what to include in observation notifications. For possible values, see  .
- `expectedValue`: A value that the key path’s specified property must equal to fulfill the expectation.

## See Also

- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, predicate: XCTKeyPathExpectation<T, V>.Predicate?)](xctkeypathexpectation/init(keypath:observedobject:options:predicate:).md)
  Creates an expectation that the system fulfills when the value of the observed property changes and satisfies the conditions of a predicate’s evaluation.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.SynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-plka.md)
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.AsynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-8noag.md)
- [XCTKeyPathExpectation.AsynchronousFilter](xctkeypathexpectation/asynchronousfilter.md)
- [XCTKeyPathExpectation.SynchronousFilter](xctkeypathexpectation/synchronousfilter.md)
- [XCTKeyPathExpectation.Predicate](xctkeypathexpectation/predicate.md)
  A function the key path expectation uses to test the value of an observed property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/init(keypath:observedobject:options:expectedvalue:))*