# delegate

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The delegate to which expectation fulfillment events will be reported.

## Declaration

```swift
weak var delegate: (any XCTWaiterDelegate)? { get set }
```

```objc
@property (weak, nullable) id<XCTWaiterDelegate> delegate;
```

## See Also

### Responding to Expectation Fulfilment
- [protocol XCTWaiterDelegate](../xctwaiterdelegate.md)
  Defines methods that are called when [`XCTWaiter`](../xctwaiter.md) expectations are fulfilled correctly or incorrectly.
- [var fulfilledExpectations: [XCTestExpectation]](./fulfilledexpectations.md)
  An array of expectations that were fulfilled, in order, up until the waiter stopped waiting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/delegate)*