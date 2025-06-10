# XCTKeyPathExpectation.Predicate

**Framework**: XCTest  
**Kind**: typealias

A function the key path expectation uses to test the value of an observed property.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
typealias Predicate = (T, NSKeyValueObservedChange<V>) async -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the change fulfills the expectation; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

A key path expectation uses this function to determine whether the value of the observed property fulfills the conditions of the expectation. The system invokes the function asyncronously on a detached task and may call the function more that once.

## Parameters

- `observedObject`: The observed object to evaluate with the property that changes.
- `change`: A value that describes the observed change.

## See Also

- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, expectedValue: V)](xctkeypathexpectation/init(keypath:observedobject:options:expectedvalue:).md)
  Creates an expectation that the system fulfills when the value of the observed property changes to an expected value.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, predicate: XCTKeyPathExpectation<T, V>.Predicate?)](xctkeypathexpectation/init(keypath:observedobject:options:predicate:).md)
  Creates an expectation that the system fulfills when the value of the observed property changes and satisfies the conditions of a predicate’s evaluation.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.SynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-plka.md)
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.AsynchronousFilter?)](xctkeypathexpectation/init(keypath:observedobject:options:filter:)-8noag.md)
- [XCTKeyPathExpectation.AsynchronousFilter](xctkeypathexpectation/asynchronousfilter.md)
- [XCTKeyPathExpectation.SynchronousFilter](xctkeypathexpectation/synchronousfilter.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/predicate)*