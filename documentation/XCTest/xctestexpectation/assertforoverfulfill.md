# assertForOverFulfill

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

Indicates that an assertion should be triggered during testing if the expectation is over-fulfilled.

## Declaration

```swift
var assertForOverFulfill: Bool { get set }
```

```objc
@property (nonatomic) BOOL assertForOverFulfill;
```

## Discussion

When [`true`](../../Swift/true.md), a call to [`fulfill()`](./fulfill%28%29.md) made after the expectation has already been fulfilled (exceeding [`expectedFulfillmentCount`](./expectedfulfillmentcount.md)) will trigger an assertion. When [`false`](../../Swift/false.md), a call to [`fulfill()`](./fulfill%28%29.md) after the expectation has already been fulfilled will have no effect.

The [`assertForOverFulfill`](./assertforoverfulfill.md) property is set to [`false`](../../Swift/false.md) by default for expectations created directly from initializers on [`XCTestExpectation`](../xctestexpectation.md) and its subclasses.

The [`assertForOverFulfill`](./assertforoverfulfill.md) property is set to [`true`](../../Swift/true.md) by default for expectations created with the following [`XCTestCase`](../xctestcase.md) convenience methods:

- [`expectation(description:)`](../xctestcase/expectation%28description%29.md)
- [`expectation(for:evaluatedWith:handler:)`](../xctestcase/expectation%28for,evaluatedwith,handler%29.md)
- [`expectation(forNotification:object:handler:)`](../xctestcase/expectation%28fornotification,object,handler%29.md)
- [`keyValueObservingExpectation(for:keyPath:expectedValue:)`](../xctestcase/keyvalueobservingexpectation%28for,keypath,expectedvalue%29.md)
- [`keyValueObservingExpectation(for:keyPath:handler:)`](../xctestcase/keyvalueobservingexpectation%28for,keypath,handler%29.md)

## See Also

### Fulfillment Count
- [var expectedFulfillmentCount: Int](./expectedfulfillmentcount.md)
  The number of times [`fulfill()`](./fulfill%28%29.md) must be called before the expectation is completely fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/assertforoverfulfill)*