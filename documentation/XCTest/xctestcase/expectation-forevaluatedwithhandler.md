# expectation(for:evaluatedWith:handler:)

**Framework**: XCTest  
**Kind**: method

Creates an expectation that the test fulfills by evaluating the predicate with the specified object.

## Declaration

```swift
func expectation(for predicate: NSPredicate, evaluatedWith object: Any?, handler: XCTNSPredicateExpectation.Handler? = nil) -> XCTestExpectation
```

#### Discussion

The expectation periodically evaluates the predicate and also may use notifications or other events to optimistically re-evaluate. The test fulfills the expectation when the predicate evaluates to [`true`](https://developer.apple.com/documentation/Swift/true).

When you use the resulting expectation from Swift and await using [`fulfillment(of:timeout:enforceOrder:)`](xctestcase/fulfillment(of:timeout:enforceorder:).md) rather than [`wait(for:)`](xctestcase/wait(for:).md), XCTest evaluates `predicate` on the main actor.

If a handler isn’t provided, the first successful evaluation of the predicate fulfills the expectation. If you provide a handler, the handler can override this default behavior to tailor the conditions that fulfill the expectation.

> **Note**:  For more control over predicate-based expectations, use [`XCTNSPredicateExpectation`](xctnspredicateexpectation.md) instead of this convenience method.

## Parameters

- `predicate`: The predicate to evaluate.
- `object`: The object XCTest evaluates the predicate against.
- `handler`: An optional handler that performs custom evaluation when   evaluates as  .

## See Also

- [func expectation(description: String) -> XCTestExpectation](xctestcase/expectation(description:).md)
  Creates a new expectation with an associated description.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/expectation(for:evaluatedwith:handler:))*