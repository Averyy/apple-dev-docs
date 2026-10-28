# removeDeliveredNotifications(withIdentifiers:)

**Framework**: User Notifications  
**Kind**: method  
**Role**: Instance Method

Removes your app’s notifications from Notification Center that match the specified identifiers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func removeDeliveredNotifications(withIdentifiers identifiers: [String])
```

```objc
- (void) removeDeliveredNotificationsWithIdentifiers:(NSArray<NSString *> *) identifiers;
```

## Discussion

Use this method to selectively remove notifications that you no longer want displayed in Notification Center. The method executes asynchronously, returning immediately and removing the specified notifications on a background thread.

## Parameters

- `identifiers`: An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which corresponds to a value in the [`identifier`](../unnotificationrequest/identifier.md) property of a [`UNNotificationRequest`](../unnotificationrequest.md) object. This method ignores the identifiers of requests whose notifications are not currently displayed in Notification Center.

## See Also

### Removing delivered notifications
- [func getDeliveredNotifications(completionHandler: ([UNNotification]) -> Void)](./getdeliverednotifications%28completionhandler%29.md)
  Fetches all of your app’s delivered notifications that are still present in Notification Center.
- [func removeAllDeliveredNotifications()](./removealldeliverednotifications%28%29.md)
  Removes all of your app’s delivered notifications from Notification Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removedeliverednotifications(withidentifiers:))*