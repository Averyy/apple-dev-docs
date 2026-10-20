# keyValueObservingExpectation(for:keyPath:expectedValue:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Creates an expectation that uses Key-Value Observing to observe a value until it matches an expected value.

**Availability**:
- iOS - Deprecated in 17.0
- iPadOS - Deprecated in 17.0
- Mac Catalyst - Deprecated in 17.0
- macOS - Deprecated in 27.0
- tvOS - Deprecated in 17.0
- visionOS - Deprecated in 1.0
- watchOS - Deprecated in 26.0

> **Deprecated**: Replaced by 'expectation(that:on:options:willEqual:)'

## Declaration

```swift
func keyValueObservingExpectation(for objectToObserve: Any, keyPath: String, expectedValue: Any?) -> XCTestExpectation
```

```objc
- (XCTestExpectation *) keyValueObservingExpectationForObject:(id) objectToObserve keyPath:(NSString *) keyPath expectedValue:(id) expectedValue;
```

#### Return Value

Creates and returns an expectation associated with the test case.

#### Discussion

Creates an [`XCTestExpectation`](../xctestexpectation.md) that uses Key Value Observing to observe changes on the provided object until the value specified by `keyPath` matches the expected value using `isEqual:`.

> **Note**:  For more control over KVO-based expectations, use [`XCTKVOExpectation`](../xctkvoexpectation.md) instead of this convenience method.

## Parameters

- `objectToObserve`: The object to observe.
- `keyPath`: The key path to observe.
- `expectedValue`: Expected value of the value specified by `keyPath`. The expectation will fulfill itself when the value at `keyPath` is equal to `expectedValue`, as tested using `isEqual:`. If `expectedValue` is `nil`, the expectation will be fulfilled by the first change to the key path of the observed object.

## See Also

### Creating Asynchronous Test Expectations
- [func expectation(description: String) -> XCTestExpectation](./expectation%28description%29.md)
  Creates a new expectation with an associated description.
- [func expectation(for: NSPredicate, evaluatedWith: Any?, handler: XCTNSPredicateExpectation.Handler?) -> XCTestExpectation](./expectation%28for,evaluatedwith,handler%29.md)
  Creates an expectation that the test fulfills by evaluating the predicate with the specified object.
- [func expectation(forNotification: NSNotification.Name, object: Any?, handler: XCTNSNotificationExpectation.Handler?) -> XCTestExpectation](./expectation%28fornotification,object,handler%29.md)
  Creates an expectation that the test fulfills when it receives a specific notification for a specified object.
- [func expectation(forNotification: NSNotification.Name, object: Any?, notificationCenter: NotificationCenter, handler: XCTNSNotificationExpectation.Handler?) -> XCTestExpectation](./expectation%28fornotification,object,notificationcenter,handler%29.md)
  Creates an expectation that the test fulfills when it receives a specific notification from a specific notification center for a specified object.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willEqual: V) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willequal%29.md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes to an expected value.
- [func keyValueObservingExpectation(for: Any, keyPath: String, handler: XCTKVOExpectation.Handler?) -> XCTestExpectation](./keyvalueobservingexpectation%28for,keypath,handler%29.md)
  Creates an expectation that uses Key-Value Observing to observe a value and respond to changes in that value by calling a provided handler.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.Predicate?) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willsatisfy%29-6itb.md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes and satisfies the conditions of a predicate’s evaluation.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.AsynchronousFilter?) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willsatisfy%29-292oj.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.SynchronousFilter?) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willsatisfy%29-85or0.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/keyvalueobservingexpectation(for:keypath:expectedvalue:))*