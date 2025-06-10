# XCTKeyPathExpectation.AsynchronousFilter

**Framework**: XCTest  
**Kind**: typealias

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

## Declaration

```swift
typealias AsynchronousFilter = (T, NSKeyValueObservedChange<V>) async -> Bool
```

## See Also

- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, expectedValue: V)](xctkeypathexpectation/init(keypath:observedobject:options:expectedvalue:).md)
  Creates an expectation that the system fulfills when the value of the observed property changes to an expected value.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, predicate: XCTKeyPathExpectation<T, V>.Predicate?)](xctkeypathexpectation/init(keypath:observedobject:options:predicate:).md)
  Creates an expectation that the system fulfills when the value of the observed property changes and satisfies the conditions of a predicate’s evaluation.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.SynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-plka.md)
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.AsynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-8noag.md)
- [XCTKeyPathExpectation.SynchronousFilter](xctkeypathexpectation/synchronousfilter.md)
- [XCTKeyPathExpectation.Predicate](xctkeypathexpectation/predicate.md)
  A function the key path expectation uses to test the value of an observed property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/asynchronousfilter)*