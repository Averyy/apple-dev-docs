# expectedFulfillmentCount

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The number of times [`fulfill()`](./fulfill%28%29.md) must be called before the expectation is completely fulfilled.

## Declaration

```swift
var expectedFulfillmentCount: Int { get set }
```

```objc
@property (nonatomic) NSUInteger expectedFulfillmentCount;
```

## Discussion

The value of [`expectedFulfillmentCount`](./expectedfulfillmentcount.md) must be greater than 0. By default, expectations have an [`expectedFulfillmentCount`](./expectedfulfillmentcount.md) of 1.

> **Note**:  The value of [`expectedFulfillmentCount`](./expectedfulfillmentcount.md) is ignored when [`isInverted`](./isinverted.md) is [`true`](../../Swift/true.md).

## See Also

### Fulfillment Count
- [var assertForOverFulfill: Bool](./assertforoverfulfill.md)
  Indicates that an assertion should be triggered during testing if the expectation is over-fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation/expectedfulfillmentcount)*