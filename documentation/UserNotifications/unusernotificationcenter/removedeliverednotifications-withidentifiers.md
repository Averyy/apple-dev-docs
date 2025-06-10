# removeDeliveredNotifications(withIdentifiers:)

**Framework**: User Notifications  
**Kind**: method

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

#### Discussion

Use this method to selectively remove notifications that you no longer want displayed in Notification Center. The method executes asynchronously, returning immediately and removing the specified notifications on a background thread.

## Parameters

- `identifiers`: An array of   objects, each of which corresponds to a value in the   property of a   object. This method ignores the identifiers of requests whose notifications are not currently displayed in Notification Center.

## See Also

- [func getDeliveredNotifications(completionHandler: ([UNNotification]) -> Void)](unusernotificationcenter/getdeliverednotifications(completionhandler:).md)
  Fetches all of your app’s delivered notifications that are still present in Notification Center.
- [func removeAllDeliveredNotifications()](unusernotificationcenter/removealldeliverednotifications.md)
  Removes all of your app’s delivered notifications from Notification Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/removedeliverednotifications(withidentifiers:))*