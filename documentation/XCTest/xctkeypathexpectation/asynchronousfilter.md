# XCTKeyPathExpectation.AsynchronousFilter

**Framework**: XCTest  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

## Declaration

```swift
typealias AsynchronousFilter = @Sendable (T, NSKeyValueObservedChange<V>) async -> Bool
```

Available when `T` inherits `NSObject`, `T` conforms to `Sendable`, and `V` conforms to `Sendable`.

## See Also

### Creating key path expectations
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, expectedValue: V)](./init%28keypath,observedobject,options,expectedvalue%29.md)
  Creates an expectation that the system fulfills when the value of the observed property changes to an expected value.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, predicate: XCTKeyPathExpectation<T, V>.Predicate?)](./init%28keypath,observedobject,options,predicate%29.md)
  Creates an expectation that the system fulfills when the value of the observed property changes and satisfies the conditions of a predicate’s evaluation.
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.SynchronousFilter?)](./init%28keypath,observedobject,options,filter%29-plka.md)
- [convenience init(keyPath: KeyPath<T, V>, observedObject: T, options: NSKeyValueObservingOptions, filter: XCTKeyPathExpectation<T, V>.AsynchronousFilter?)](./init%28keypath,observedobject,options,filter%29-8noag.md)
- [XCTKeyPathExpectation.SynchronousFilter](./synchronousfilter.md)
- [XCTKeyPathExpectation.Predicate](./predicate.md)
  A function the key path expectation uses to test the value of an observed property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctkeypathexpectation/asynchronousfilter)*