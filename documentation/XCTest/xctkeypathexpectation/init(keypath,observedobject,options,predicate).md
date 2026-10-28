# init(keyPath:observedObject:options:predicate:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an expectation that the system fulfills when the value of the observed property changes and satisfies the conditions of a predicate’s evaluation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

> **Deprecated**: T and V must be Sendable when used with an asynchronous filtering function.

## Declaration

```swift
convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions = [.initial, .new, .old], predicate: XCTKeyPathExpectation<T, V>.Predicate? = nil)
```

## Discussion

Use this initializer to create an expectation that observes changes on the observed object until the predicate returns [`true`](../../Swift/true.md), fulfilling the expectation.

## Parameters

- `keyPath`: The key path for the observed property, relative to the observed object.
- `observedObject`: The object to observe the key path on.
- `options`: A combination of values that specify what to include in observation notifications. For possible values, see [`NSKeyValueObservingOptions`](../../Foundation/nskeyvalueobservingoptions.md).
- `predicate`: A closure that evaluates the value of the observed property. If `nil`, the first observed change fulfills the expectation.

## See Also

### Creating key path expectations
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, expectedValue: V)](./init%28keypath,observedobject,options,expectedvalue%29.md)
  Creates an expectation that the system fulfills when the value of the observed property changes to an expected value.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.SynchronousFilter?)](./init%28keypath,observedobject,options,filter%29-plka.md)
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.AsynchronousFilter?)](./init%28keypath,observedobject,options,filter%29-8noag.md)
- [XCTKeyPathExpectation.AsynchronousFilter](./asynchronousfilter.md)
- [XCTKeyPathExpectation.SynchronousFilter](./synchronousfilter.md)
- [XCTKeyPathExpectation.Predicate](./predicate.md)
  A function the key path expectation uses to test the value of an observed property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/init(keypath:observedobject:options:predicate:))*