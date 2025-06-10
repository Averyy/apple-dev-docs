# removeAllDeliveredNotifications()

**Framework**: User Notifications  
**Kind**: method

Removes all of your app’s delivered notifications from Notification Center.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func removeAllDeliveredNotifications()
```

#### Discussion

Use this method to remove all of your app’s delivered notifications from Notification Center. The method executes asynchronously, returning immediately and removing the identifiers on a background thread. This method does not affect any notification requests that are scheduled, but have not yet been delivered.

## See Also

- [func getDeliveredNotifications(completionHandler: ([UNNotification]) -> Void)](unusernotificationcenter/getdeliverednotifications(completionhandler:).md)
  Fetches all of your app’s delivered notifications that are still present in Notification Center.
- [func removeDeliveredNotifications(withIdentifiers: [String])](unusernotificationcenter/removedeliverednotifications(withidentifiers:).md)
  Removes your app’s notifications from Notification Center that match the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removealldeliverednotifications())*