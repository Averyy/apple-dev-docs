# init(keyPath:observedObject:options:predicate:)

**Framework**: XCTest  
**Kind**: init

Creates an expectation that the system fulfills when the value of the observed property changes and satisfies the conditions of a predicate’s evaluation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- Unknown ?+ - Deprecated
- tvOS 13.0+

## Declaration

```swift
convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions = [.initial, .new, .old], predicate: XCTKeyPathExpectation<T, V>.Predicate? = nil)
```

#### Discussion

Use this initializer to create an expectation that observes changes on the observed object until the predicate returns [`true`](https://developer.apple.com/documentation/swift/true), fulfilling the expectation.

## Parameters

- `keyPath`: The key path for the observed property, relative to the observed object.
- `observedObject`: The object to observe the key path on.
- `options`: A combination of values that specify what to include in observation notifications. For possible values, see  .
- `predicate`: A closure that evaluates the value of the observed property. If  , the first observed change fulfills the expectation.

## See Also

- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, expectedValue: V)](xctkeypathexpectation/init(keypath:observedobject:options:expectedvalue:).md)
  Creates an expectation that the system fulfills when the value of the observed property changes to an expected value.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.SynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-plka.md)
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.AsynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-8noag.md)
- [XCTKeyPathExpectation.AsynchronousFilter](xctkeypathexpectation/asynchronousfilter.md)
- [XCTKeyPathExpectation.SynchronousFilter](xctkeypathexpectation/synchronousfilter.md)
- [XCTKeyPathExpectation.Predicate](xctkeypathexpectation/predicate.md)
  A function the key path expectation uses to test the value of an observed property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/init(keypath:observedobject:options:predicate:))*