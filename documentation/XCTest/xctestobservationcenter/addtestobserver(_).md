# addTestObserver(_:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Registers an object conforming to [`XCTestObservation`](../xctestobservation.md) as an observer for the current test session.

## Declaration

```swift
func addTestObserver(_ testObserver: any XCTestObservation)
```

```objc
- (void) addTestObserver:(id<XCTestObservation>) testObserver;
```

#### Discussion

Observers may be added at any time, but will not receive events that occurred before they were registered. The observation center maintains a strong reference to observers.Events may be delivered to observers in any order. Given observers A and B, A may be notified of a test failure before or after B. Any ordering dependencies or serialization requirements must be managed by clients.

## See Also

### Managing Observers
- [func removeTestObserver(any XCTestObservation)](./removetestobserver%28_%29.md)
  Unregisters an object conforming to [`XCTestObservation`](../xctestobservation.md) as an observer for the current test session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservationcenter/addtestobserver(_:))*