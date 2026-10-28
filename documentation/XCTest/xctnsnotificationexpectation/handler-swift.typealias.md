# XCTNSNotificationExpectation.Handler

**Framework**: XCTest  
**Kind**: typealias  
**Role**: Type Alias

A custom handler to be called when a matching notification is received.

## Declaration

```swift
typealias Handler = @Sendable (Notification) -> Bool
```

```c
typedef _Bool (^)(NSNotification *) XCNotificationExpectationHandler;
```

## Return Value

Your custom handler should return [`true`](../../Swift/true.md) if the expectation is considered fulfilled after the notification is received, otherwise [`false`](../../Swift/false.md).

## Parameters

- `notification`: The notification object.

## See Also

### Custom Notification Evaluation
- [var handler: XCTNSNotificationExpectation.Handler?](./handler-swift.property.md)
  An optional handler that performs custom evaluation of matching notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctnsnotificationexpectation/handler-swift.typealias)*