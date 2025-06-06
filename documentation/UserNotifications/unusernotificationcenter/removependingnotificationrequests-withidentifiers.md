# removePendingNotificationRequests(withIdentifiers:)

**Framework**: Usernotifications  
**Kind**: method

Removes your app’s local notifications that are pending and match the specified identifiers.

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
func removePendingNotificationRequests(withIdentifiers identifiers: [String])
```

#### Discussion

This method executes asynchronously, removing the pending notification requests on a secondary thread.

```swift
let center = UNUserNotificationCenter.current()
center.removePendingNotificationRequests(withIdentifiers: ["com.example.mynotification"])
```

## Parameters

- `identifiers`: An array of   objects, each of which contains the   of an active   object. If the identifier belongs to a non repeating request, and the trigger condition for that request has already been met, this method ignores the identifier.

## See Also

- [func add(UNNotificationRequest, withCompletionHandler: (((any Error)?) -> Void)?)](unusernotificationcenter/add(_:withcompletionhandler:).md)
  Schedules the delivery of a local notification.
- [func getPendingNotificationRequests(completionHandler: ([UNNotificationRequest]) -> Void)](unusernotificationcenter/getpendingnotificationrequests(completionhandler:).md)
  Fetches all of your app’s local notifications that are pending delivery.
- [func removeAllPendingNotificationRequests()](unusernotificationcenter/removeallpendingnotificationrequests.md)
  Removes all of your app’s pending local notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removependingnotificationrequests(withidentifiers:))*