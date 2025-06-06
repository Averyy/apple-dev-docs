# XCTDarwinNotificationExpectation.Handler

**Framework**: Xctest  
**Kind**: typealias

A custom handler to be called when a matching notification is received.

## Declaration

```swift
typealias Handler = () -> Bool
```

#### Return Value

Your custom handler should return [`true`](https://developer.apple.com/documentation/swift/true) if the expectation is considered fulfilled after the notification is received, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var handler: XCTDarwinNotificationExpectation.Handler?](xctdarwinnotificationexpectation/handler-swift.property.md)
  An optional handler that performs custom evaluation of matching notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctdarwinnotificationexpectation/handler-swift.typealias)*