# expectation(that:on:options:willSatisfy:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Creates an expectation using key-value observing the test fulfills when the value of an observed property changes and satisfies the conditions of a predicate’s evaluation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+

> **Deprecated**: T and V must be Sendable for use in an asynchronous filtering function. Use [`expectation(that:on:options:willSatisfy:)`](./expectation%28that,on,options,willsatisfy%29-292oj.md) to provide an asynchronous filtering function and [`expectation(that:on:options:willSatisfy:)`](./expectation%28that,on,options,willsatisfy%29-85or0.md) for a syncronous filtering function instead.

## Declaration

```swift
func expectation<T, V>(that keyPath: KeyPath<T, V>, on observedObject: T, options: NSKeyValueObservingOptions = [.initial, .new, .old], willSatisfy predicate: XCTKeyPathExpectation<T, V>.Predicate? = nil) -> XCTKeyPathExpectation<T, V> where T : NSObject
```

## Return Value

Creates and returns an expectation for the test case.

## Parameters

- `keyPath`: The key path for the observed property, relative to the observed object.
- `observedObject`: The object to observe the property on.
- `options`: A combination of values that specify what to include in observation notifications. For possible values, see [`NSKeyValueObservingOptions`](../../Foundation/nskeyvalueobservingoptions.md).
- `predicate`: A closure that evaluates the observed object. If `nil`, the first observed change fulfills the expectation.

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
- [func keyValueObservingExpectation(for: Any, keyPath: String, expectedValue: Any?) -> XCTestExpectation](./keyvalueobservingexpectation%28for,keypath,expectedvalue%29.md)
  Creates an expectation that uses Key-Value Observing to observe a value until it matches an expected value.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willEqual: V) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willequal%29.md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes to an expected value.
- [func keyValueObservingExpectation(for: Any, keyPath: String, handler: XCTKVOExpectation.Handler?) -> XCTestExpectation](./keyvalueobservingexpectation%28for,keypath,handler%29.md)
  Creates an expectation that uses Key-Value Observing to observe a value and respond to changes in that value by calling a provided handler.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.AsynchronousFilter?) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willsatisfy%29-292oj.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.SynchronousFilter?) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willsatisfy%29-85or0.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/expectation(that:on:options:willsatisfy:)-6itb)*