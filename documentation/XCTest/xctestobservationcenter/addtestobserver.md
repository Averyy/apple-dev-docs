# addTestObserver(_:)

**Framework**: Xctest  
**Kind**: method

Registers an object conforming to [`XCTestObservation`](xctestobservation.md) as an observer for the current test session.

## Declaration

```swift
func addTestObserver(_ testObserver: any XCTestObservation)
```

#### Discussion

Observers may be added at any time, but will not receive events that occurred before they were registered. The observation center maintains a strong reference to observers.Events may be delivered to observers in any order. Given observers A and B, A may be notified of a test failure before or after B. Any ordering dependencies or serialization requirements must be managed by clients.

## See Also

- [func removeTestObserver(any XCTestObservation)](xctestobservationcenter/removetestobserver(_:).md)
  Unregisters an object conforming to [`XCTestObservation`](xctestobservation.md) as an observer for the current test session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservationcenter/addtestobserver(_:))*