# expectation(description:)

**Framework**: Xctest  
**Kind**: method

Creates a new expectation with an associated description.

## Declaration

```swift
func expectation(description: String) -> XCTestExpectation
```

#### Discussion

Use this method to create [`XCTestExpectation`](xctestexpectation.md) instances that can be fulfilled when asynchronous tasks in your tests complete.

To fulfill an expectation that was created with [`expectation(description:)`](xctestcase/expectation(description:).md), call the expectation’s [`fulfill()`](xctestexpectation/fulfill().md) method when the asynchronous task in your test has completed.

## Parameters

- `description`: A string to display in the test log for this expectation, to help diagnose failures.

## See Also

- [func expectation(for: NSPredicate, evaluatedWith: Any?, handler: XCTNSPredicateExpectation.Handler?) -> XCTestExpectation](xctestcase/expectation(for:evaluatedwith:handler:).md)
  Creates an expectation that the test fulfills by evaluating the predicate with the specified object.
- [func expectation(forNotification: NSNotification.Name, object: Any?, handler: XCTNSNotificationExpectation.Handler?) -> XCTestExpectation](xctestcase/expectation(fornotification:object:handler:).md)
  Creates an expectation that the test fulfills when it receives a specific notification for a specified object.
- [func expectation(forNotification: NSNotification.Name, object: Any?, notificationCenter: NotificationCenter, handler: XCTNSNotificationExpectation.Handler?) -> XCTestExpectation](xctestcase/expectation(fornotification:object:notificationcenter:handler:).md)
  Creates an expectation that the test fulfills when it receives a specific notification from a specific notification center for a specified object.
- [func keyValueObservingExpectation(for: Any, keyPath: String, expectedValue: Any?) -> XCTestExpectation](xctestcase/keyvalueobservingexpectation(for:keypath:expectedvalue:).md)
  Creates an expectation that uses Key-Value Observing to observe a value until it matches an expected value.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willEqual: V) -> XCTKeyPathExpectation<T, V>](xctestcase/expectation(that:on:options:willequal:).md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes to an expected value.
- [func keyValueObservingExpectation(for: Any, keyPath: String, handler: XCTKVOExpectation.Handler?) -> XCTestExpectation](xctestcase/keyvalueobservingexpectation(for:keypath:handler:).md)
  Creates an expectation that uses Key-Value Observing to observe a value and respond to changes in that value by calling a provided handler.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.Predicate?) -> XCTKeyPathExpectation<T, V>](xctestcase/expectation(that:on:options:willsatisfy:)-6itb.md)
  Creates an expectation using key-value observing the test fulfills when the value of an observed property changes and satisfies the conditions of a predicate’s evaluation.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.AsynchronousFilter?) -> XCTKeyPathExpectation<T, V>](xctestcase/expectation(that:on:options:willsatisfy:)-292oj.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.
- [func expectation<T, V>(that: KeyPath<T, V>, on: T, options: NSKeyValueObservingOptions, willSatisfy: XCTKeyPathExpectation<T, V>.SynchronousFilter?) -> XCTKeyPathExpectation<T, V>](xctestcase/expectation(that:on:options:willsatisfy:)-85or0.md)
  Creates an expectation using key-value observing to monitor changes to a given key path on a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/expectation(description:))*