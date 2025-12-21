# assertForOverFulfill

**Framework**: XCTest  
**Kind**: property

Indicates that an assertion should be triggered during testing if the expectation is over-fulfilled.

## Declaration

```swift
var assertForOverFulfill: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/Swift/true), a call to [`fulfill()`](xctestexpectation/fulfill().md) made after the expectation has already been fulfilled (exceeding [`expectedFulfillmentCount`](xctestexpectation/expectedfulfillmentcount.md)) will trigger an assertion. When [`false`](https://developer.apple.com/documentation/Swift/false), a call to [`fulfill()`](xctestexpectation/fulfill().md) after the expectation has already been fulfilled will have no effect.

The [`assertForOverFulfill`](xctestexpectation/assertforoverfulfill.md) property is set to [`false`](https://developer.apple.com/documentation/Swift/false) by default for expectations created directly from initializers on [`XCTestExpectation`](xctestexpectation.md) and its subclasses.

The [`assertForOverFulfill`](xctestexpectation/assertforoverfulfill.md) property is set to [`true`](https://developer.apple.com/documentation/Swift/true) by default for expectations created with the following [`XCTestCase`](xctestcase.md) convenience methods:

- [`expectation(description:)`](xctestcase/expectation(description:).md)
- [`expectation(for:evaluatedWith:handler:)`](xctestcase/expectation(for:evaluatedwith:handler:).md)
- [`expectation(forNotification:object:handler:)`](xctestcase/expectation(fornotification:object:handler:).md)
- [`keyValueObservingExpectation(for:keyPath:expectedValue:)`](xctestcase/keyvalueobservingexpectation(for:keypath:expectedvalue:).md)
- [`keyValueObservingExpectation(for:keyPath:handler:)`](xctestcase/keyvalueobservingexpectation(for:keypath:handler:).md)

## See Also

- [var expectedFulfillmentCount: Int](xctestexpectation/expectedfulfillmentcount.md)
  The number of times [`fulfill()`](xctestexpectation/fulfill().md) must be called before the expectation is completely fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/assertforoverfulfill)*