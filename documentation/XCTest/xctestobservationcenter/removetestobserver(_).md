# removeTestObserver(_:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Unregisters an object conforming to [`XCTestObservation`](../xctestobservation.md) as an observer for the current test session.

## Declaration

```swift
func removeTestObserver(_ testObserver: any XCTestObservation)
```

```objc
- (void) removeTestObserver:(id<XCTestObservation>) testObserver;
```

## See Also

### Managing Observers
- [func addTestObserver(any XCTestObservation)](./addtestobserver%28_%29.md)
  Registers an object conforming to [`XCTestObservation`](../xctestobservation.md) as an observer for the current test session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservationcenter/removetestobserver(_:))*