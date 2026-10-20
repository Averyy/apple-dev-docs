# XCTKeyPathExpectation.Predicate

**Framework**: XCTest  
**Kind**: typealias  
**Role**: Type Alias

A function the key path expectation uses to test the value of an observed property.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

> **Deprecated**: T and V must be Sendable when used with an asynchronous filtering function.

## Declaration

```swift
typealias Predicate = @Sendable (T, NSKeyValueObservedChange<V>) async -> Bool
```

#### Return Value

Returns [`true`](../../Swift/true.md) if the change fulfills the expectation; otherwise, [`false`](../../Swift/false.md).

#### Discussion

A key path expectation uses this function to determine whether the value of the observed property fulfills the conditions of the expectation. The system invokes the function asyncronously on a detached task and may call the function more that once.

## Parameters

- `observedObject`: The observed object to evaluate with the property that changes.
- `change`: A value that describes the observed change.

## See Also

### Creating key path expectations
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, expectedValue: V)](./init%28keypath,observedobject,options,expectedvalue%29.md)
  Creates an expectation that the system fulfills when the value of the observed property changes to an expected value.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, predicate: XCTKeyPathExpectation<T, V>.Predicate?)](./init%28keypath,observedobject,options,predicate%29.md)
  Creates an expectation that the system fulfills when the value of the observed property changes and satisfies the conditions of a predicate’s evaluation.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.SynchronousFilter?)](./init%28keypath,observedobject,options,filter%29-plka.md)
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.AsynchronousFilter?)](./init%28keypath,observedobject,options,filter%29-8noag.md)
- [XCTKeyPathExpectation.AsynchronousFilter](./asynchronousfilter.md)
- [XCTKeyPathExpectation.SynchronousFilter](./synchronousfilter.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/predicate)*