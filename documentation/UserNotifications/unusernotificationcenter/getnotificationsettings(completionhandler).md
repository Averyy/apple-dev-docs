# getNotificationSettings(completionHandler:)

**Framework**: User Notifications  
**Kind**: method  
**Role**: Instance Method

Retrieves the authorization and feature-related settings for your app.

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
func getNotificationSettings(completionHandler: @escaping @Sendable (UNNotificationSettings) -> Void)
```

```swift
func notificationSettings() async -> UNNotificationSettings
```

```objc
- (void) getNotificationSettingsWithCompletionHandler:(void (^)(UNNotificationSettings *settings)) completionHandler;
```

## Mentions

- [Asking permission to use notifications](../asking-permission-to-use-notifications.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func notificationSettings() async -> UNNotificationSettings
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Use this method to determine the user interactions and notification-related features that the system authorizes your app to use. You might then use this information to enable or disable specific notification-related features of your app.

```swift
let center = UNUserNotificationCenter.current()
let settings = await center.notificationSettings()
// Add code here to inspect or act on the settings.
```

When the user initially grants authorization to your app, the system gives your app a set of default notification-related settings. The user may change those settings at any time to enable or disable specific capabilities. For example, the user might disable the playing of sounds when a notification arrives.

## Parameters

- `completionHandler`: The block to execute asynchronously with the results. Your app may execute this block on a background thread. The block has no return value and takes the following parameter:

  - **settings**: The [`UNNotificationSettings`](../unnotificationsettings.md) object containing the current authorization settings for your app.

## See Also

### Managing the notification center
- [class func current() -> UNUserNotificationCenter](./current%28%29.md)
  Returns your app’s notification center.
- [func setBadgeCount(Int, withCompletionHandler: (((any Error)?) -> Void)?)](./setbadgecount%28_,withcompletionhandler%29.md)
  Updates the badge count for your app’s icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/getnotificationsettings(completionhandler:))*