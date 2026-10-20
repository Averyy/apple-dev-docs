# XCTWaiter.Result.interrupted

**Framework**: XCTest  
**Kind**: case  
**Role**: Case

The waiter was interrupted prior to its expectations being fulfilled or timing out.

## Declaration

```swift
case interrupted
```

```c
XCTWaiterResultInterrupted
```

#### Discussion

This occurs when an “outer” waiter times out, resulting in any waiters nested inside it being interrupted to allow the call stack to quickly unwind.

## See Also

### Result States
- [XCTWaiter.Result.completed](./completed.md)
  All of the waiter’s expectations were fulfilled successfully.
- [XCTWaiter.Result.timedOut](./timedout.md)
  The waiter timed out before all of its expectations were fulfilled.
- [XCTWaiter.Result.incorrectOrder](./incorrectorder.md)
  The waiter’s expectations were not fulfilled in the required order.
- [XCTWaiter.Result.invertedFulfillment](./invertedfulfillment.md)
  An inverted expectation was fulfilled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctwaiter/result/interrupted)*