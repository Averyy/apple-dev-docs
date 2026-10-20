# XCTestExpectation

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An expected outcome in an asynchronous test.

## Declaration

```swift
class XCTestExpectation
```

```objc
@interface XCTestExpectation : NSObject
```

## Topics

### Creating Expectations
- [init(description: String)](./xctestexpectation/init%28description%29.md)
  Creates a new [`XCTestExpectation`](./xctestexpectation.md) with the provided description.
- [var expectationDescription: String](./xctestexpectation/expectationdescription.md)
  A human readable string used to describe the expectation in log output and test reports.
### Fulfilling Expectations
- [func fulfill()](./xctestexpectation/fulfill%28%29.md)
  Marks the expectation as having been met.
### Fulfillment Count
- [var expectedFulfillmentCount: Int](./xctestexpectation/expectedfulfillmentcount.md)
  The number of times [`fulfill()`](./xctestexpectation/fulfill%28%29.md) must be called before the expectation is completely fulfilled.
- [var assertForOverFulfill: Bool](./xctestexpectation/assertforoverfulfill.md)
  Indicates that an assertion should be triggered during testing if the expectation is over-fulfilled.
### Unintended Expectations
- [var isInverted: Bool](./xctestexpectation/isinverted.md)
  Indicates that the expectation is not intended to happen.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [XCTDarwinNotificationExpectation](./xctdarwinnotificationexpectation.md)
- [XCTKVOExpectation](./xctkvoexpectation.md)
- [XCTKeyPathExpectation](./xctkeypathexpectation.md)
- [XCTNSNotificationExpectation](./xctnsnotificationexpectation.md)
- [XCTNSPredicateExpectation](./xctnspredicateexpectation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestexpectation)*