# XCTestExpectation

**Framework**: XCTest  
**Kind**: class

An expected outcome in an asynchronous test.

## Declaration

```swift
class XCTestExpectation
```

## Topics

### Creating Expectations
- [init(description: String)](xctestexpectation/init(description:).md)
  Creates a new [`XCTestExpectation`](xctestexpectation.md) with the provided description.
- [var expectationDescription: String](xctestexpectation/expectationdescription.md)
  A human readable string used to describe the expectation in log output and test reports.
### Fulfilling Expectations
- [func fulfill()](xctestexpectation/fulfill.md)
  Marks the expectation as having been met.
### Fulfillment Count
- [var expectedFulfillmentCount: Int](xctestexpectation/expectedfulfillmentcount.md)
  The number of times [`fulfill()`](xctestexpectation/fulfill().md) must be called before the expectation is completely fulfilled.
- [var assertForOverFulfill: Bool](xctestexpectation/assertforoverfulfill.md)
  Indicates that an assertion should be triggered during testing if the expectation is over-fulfilled.
### Unintended Expectations
- [var isInverted: Bool](xctestexpectation/isinverted.md)
  Indicates that the expectation is not intended to happen.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [XCTDarwinNotificationExpectation](xctdarwinnotificationexpectation.md)
- [XCTKVOExpectation](xctkvoexpectation.md)
- [XCTKeyPathExpectation](xctkeypathexpectation.md)
- [XCTNSNotificationExpectation](xctnsnotificationexpectation.md)
- [XCTNSPredicateExpectation](xctnspredicateexpectation.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation)*