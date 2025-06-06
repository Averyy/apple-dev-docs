# current()

**Framework**: Usernotifications  
**Kind**: method

Returns your app’s notification center.

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
class func current() -> UNUserNotificationCenter
```

#### Return Value

The notification center object to use.

#### Discussion

Always use this method to retrieve the shared notification center object for your app. Do not try to create instances of the [`UNUserNotificationCenter`](unusernotificationcenter.md) class directly.

## See Also

- [func getNotificationSettings(completionHandler: (UNNotificationSettings) -> Void)](unusernotificationcenter/getnotificationsettings(completionhandler:).md)
  Retrieves the authorization and feature-related settings for your app.
- [func setBadgeCount(Int, withCompletionHandler: (((any Error)?) -> Void)?)](unusernotificationcenter/setbadgecount(_:withcompletionhandler:).md)
  Updates the badge count for your app’s icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/current())*