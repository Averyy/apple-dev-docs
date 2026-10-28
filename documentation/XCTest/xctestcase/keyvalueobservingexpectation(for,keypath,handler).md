# keyValueObservingExpectation(for:keyPath:handler:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Creates an expectation that uses Key-Value Observing to observe a value and respond to changes in that value by calling a provided handler.

**Availability**:
- iOS - Deprecated in 17.0
- iPadOS - Deprecated in 17.0
- Mac Catalyst - Deprecated in 17.0
- macOS - Deprecated in 27.0
- tvOS - Deprecated in 17.0
- visionOS - Deprecated in 1.0
- watchOS - Deprecated in 26.0

> **Deprecated**: Replaced by 'expectation(that:on:options:willSatisfy:)'

## Declaration

```swift
func keyValueObservingExpectation(for objectToObserve: Any, keyPath: String, handler: XCTKVOExpectation.Handler? = nil) -> XCTestExpectation
```

```objc
- (XCTestExpectation *) keyValueObservingExpectationForObject:(id) objectToObserve keyPath:(NSString *) keyPath handler:(XCKeyValueObservingExpectationHandler) handler;
```

## Discussion

Creates an [`XCTestExpectation`](../xctestexpectation.md) that uses Key Value Observing to observe changes on the value specified by `keyPath` on the provided object.

When the tests detects changes to the value, it calls the `handler` block to assess the new value to see if the change fulfills the expectation. Every key-value observing change runs the handler block until it either returns [`true`](../../Swift/true.md) (to fulfill the expectation), or the wait times out.

You can use [`XCTAssert`](../xctassert.md) and related APIs in the block to report a failure.

> **Note**:  For more control over KVO-based expectations, use [`XCTKVOExpectation`](../xctkvoexpectation.md) instead of this convenience method.

## Parameters

- `objectToObserve`: The object to observe.
- `keyPath`: The key path to observe.
- `handler`: An optional [`XCTKVOExpectation.Handler`](../xctkvoexpectation/handler-swift.typealias.md) block. If you don’t provide a handler block, the first change to the key path of the observed object fulfills the expectation.

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
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.Predicate?) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willsatisfy%29-6itb.md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes and satisfies the conditions of a predicate’s evaluation.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.AsynchronousFilter?) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willsatisfy%29-292oj.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.SynchronousFilter?) -> XCTKeyPathExpectation<T, V>](./expectation%28that,on,options,willsatisfy%29-85or0.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/keyvalueobservingexpectation(for:keypath:handler:))*