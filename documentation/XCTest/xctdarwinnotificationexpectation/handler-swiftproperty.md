# handler

**Framework**: Xctest  
**Kind**: property

An optional handler that performs custom evaluation of matching notifications.

## Declaration

```swift
var handler: XCTDarwinNotificationExpectation.Handler? { get set }
```

#### Discussion

If provided, the custom handler will be queried each time a matching notification is received to determine whether the expectation should be fulfilled. This allows the handler to check Darwin state variables or perform other logic beyond simply verifying that the notification has been received.

## See Also

- [XCTDarwinNotificationExpectation.Handler](xctdarwinnotificationexpectation/handler-swift.typealias.md)
  A custom handler to be called when a matching notification is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctdarwinnotificationexpectation/handler-swift.property)*