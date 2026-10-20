# removeAllPendingNotificationRequests()

**Framework**: User Notifications  
**Kind**: method  
**Role**: Instance Method

Removes all of your app’s pending local notifications.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func removeAllPendingNotificationRequests()
```

```objc
- (void) removeAllPendingNotificationRequests;
```

#### Discussion

This method executes asynchronously, removing all pending notification requests on a secondary thread.

```swift
let center = UNUserNotificationCenter.current()
center.removeAllPendingNotificationRequests()
```

## See Also

### Scheduling notifications
- [func add(UNNotificationRequest, withCompletionHandler: (((any Error)?) -> Void)?)](./add%28_,withcompletionhandler%29.md)
  Schedules the delivery of a local notification.
- [func getPendingNotificationRequests(completionHandler: ([UNNotificationRequest]) -> Void)](./getpendingnotificationrequests%28completionhandler%29.md)
  Fetches all of your app’s local notifications that are pending delivery.
- [func removePendingNotificationRequests(withIdentifiers: [String])](./removependingnotificationrequests%28withidentifiers%29.md)
  Removes your app’s local notifications that are pending and match the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removeallpendingnotificationrequests())*