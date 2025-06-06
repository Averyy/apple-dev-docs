# fulfilledExpectations

**Framework**: Xctest  
**Kind**: property

An array of expectations that were fulfilled, in order, up until the waiter stopped waiting.

## Declaration

```swift
var fulfilledExpectations: [XCTestExpectation] { get }
```

#### Discussion

The array will be empty until the waiter has started waiting, even if expectations have already been fulfilled. Expectations fulfilled after the waiter stops waiting will not be in the array.

## See Also

- [var delegate: (any XCTWaiterDelegate)?](xctwaiter/delegate.md)
  The delegate to which expectation fulfillment events will be reported.
- [protocol XCTWaiterDelegate](xctwaiterdelegate.md)
  Defines methods that are called when [`XCTWaiter`](xctwaiter.md) expectations are fulfilled correctly or incorrectly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/fulfilledexpectations)*