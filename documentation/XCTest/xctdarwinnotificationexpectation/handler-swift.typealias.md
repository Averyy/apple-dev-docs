# XCTDarwinNotificationExpectation.Handler

**Framework**: XCTest  
**Kind**: typealias  
**Role**: Type Alias

A custom handler to be called when a matching notification is received.

## Declaration

```swift
typealias Handler = @Sendable () -> Bool
```

```c
typedef _Bool (^)(void) XCTDarwinNotificationExpectationHandler;
```

#### Return Value

Your custom handler should return [`true`](../../Swift/true.md) if the expectation is considered fulfilled after the notification is received, otherwise [`false`](../../Swift/false.md).

## See Also

### Custom Notification Evaluation
- [var handler: XCTDarwinNotificationExpectation.Handler?](./handler-swift.property.md)
  An optional handler that performs custom evaluation of matching notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctdarwinnotificationexpectation/handler-swift.typealias)*