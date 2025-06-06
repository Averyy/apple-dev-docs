# XCTWaiter.Result.interrupted

**Framework**: Xctest  
**Kind**: case

The waiter was interrupted prior to its expectations being fulfilled or timing out.

## Declaration

```swift
case interrupted
```

#### Discussion

This occurs when an “outer” waiter times out, resulting in any waiters nested inside it being interrupted to allow the call stack to quickly unwind.

## See Also

- [XCTWaiter.Result.completed](xctwaiter/result/completed.md)
  All of the waiter’s expectations were fulfilled successfully.
- [XCTWaiter.Result.timedOut](xctwaiter/result/timedout.md)
  The waiter timed out before all of its expectations were fulfilled.
- [XCTWaiter.Result.incorrectOrder](xctwaiter/result/incorrectorder.md)
  The waiter’s expectations were not fulfilled in the required order.
- [XCTWaiter.Result.invertedFulfillment](xctwaiter/result/invertedfulfillment.md)
  An inverted expectation was fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/result/interrupted)*