# expectedFulfillmentCount

**Framework**: XCTest  
**Kind**: property

The number of times [`fulfill()`](xctestexpectation/fulfill().md) must be called before the expectation is completely fulfilled.

## Declaration

```swift
var expectedFulfillmentCount: Int { get set }
```

#### Discussion

The value of [`expectedFulfillmentCount`](xctestexpectation/expectedfulfillmentcount.md) must be greater than 0. By default, expectations have an [`expectedFulfillmentCount`](xctestexpectation/expectedfulfillmentcount.md) of 1.

> **Note**:  The value of [`expectedFulfillmentCount`](xctestexpectation/expectedfulfillmentcount.md) is ignored when [`isInverted`](xctestexpectation/isinverted.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var assertForOverFulfill: Bool](xctestexpectation/assertforoverfulfill.md)
  Indicates that an assertion should be triggered during testing if the expectation is over-fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/expectedfulfillmentcount)*