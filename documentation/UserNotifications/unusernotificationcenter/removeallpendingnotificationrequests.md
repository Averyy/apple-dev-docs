# removeAllPendingNotificationRequests()

**Framework**: User Notifications  
**Kind**: method

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

#### Discussion

This method executes asynchronously, removing all pending notification requests on a secondary thread.

```swift
let center = UNUserNotificationCenter.current()
center.removeAllPendingNotificationRequests()
```

## See Also

- [func add(UNNotificationRequest, withCompletionHandler: (((any Error)?) -> Void)?)](unusernotificationcenter/add(_:withcompletionhandler:).md)
  Schedules the delivery of a local notification.
- [func getPendingNotificationRequests(completionHandler: ([UNNotificationRequest]) -> Void)](unusernotificationcenter/getpendingnotificationrequests(completionhandler:).md)
  Fetches all of your app’s local notifications that are pending delivery.
- [func removePendingNotificationRequests(withIdentifiers: [String])](unusernotificationcenter/removependingnotificationrequests(withidentifiers:).md)
  Removes your app’s local notifications that are pending and match the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removeallpendingnotificationrequests())*