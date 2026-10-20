# removePendingNotificationRequests(withIdentifiers:)

**Framework**: User Notifications  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removePendingNotificationRequestsWithIdentifiers:(NSArray<NSString *> *) identifiers;
```

#### Discussion

This method executes asynchronously, removing the pending notification requests on a secondary thread.

```swift
let center = UNUserNotificationCenter.current()
center.removePendingNotificationRequests(withIdentifiers: ["com.example.mynotification"])
```

## Parameters

- `identifiers`: An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains the [`identifier`](../unnotificationrequest/identifier.md) of an active [`UNNotificationRequest`](../unnotificationrequest.md) object. If the identifier belongs to a non repeating request, and the trigger condition for that request has already been met, this method ignores the identifier.

## See Also

### Scheduling notifications
- [func add(UNNotificationRequest, withCompletionHandler: (((any Error)?) -> Void)?)](./add%28_,withcompletionhandler%29.md)
  Schedules the delivery of a local notification.
- [func getPendingNotificationRequests(completionHandler: ([UNNotificationRequest]) -> Void)](./getpendingnotificationrequests%28completionhandler%29.md)
  Fetches all of your app’s local notifications that are pending delivery.
- [func removeAllPendingNotificationRequests()](./removeallpendingnotificationrequests%28%29.md)
  Removes all of your app’s pending local notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removependingnotificationrequests(withidentifiers:))*