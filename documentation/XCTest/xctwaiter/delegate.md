# delegate

**Framework**: XCTest  
**Kind**: property

The delegate to which expectation fulfillment events will be reported.

## Declaration

```swift
weak var delegate: (any XCTWaiterDelegate)? { get set }
```

## See Also

- [protocol XCTWaiterDelegate](xctwaiterdelegate.md)
  Defines methods that are called when [`XCTWaiter`](xctwaiter.md) expectations are fulfilled correctly or incorrectly.
- [var fulfilledExpectations: [XCTestExpectation]](xctwaiter/fulfilledexpectations.md)
  An array of expectations that were fulfilled, in order, up until the waiter stopped waiting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/delegate)*