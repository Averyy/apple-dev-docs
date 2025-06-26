# UNUserNotificationCenter

**Framework**: User Notifications  
**Kind**: class

The central object for managing notification-related activities for your app or app extension.

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
class UNUserNotificationCenter
```

## Mentions

- [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md)
- [Asking permission to use notifications](asking-permission-to-use-notifications.md)
- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)

#### Overview

Use the shared [`UNUserNotificationCenter`](unusernotificationcenter.md) object to manage all notification-related behaviors in your app or app extension. Specifically, use this object to do the following:

- Request authorization to interact with the user through alerts, sounds, and icon badges. See [`Asking permission to use notifications`](asking-permission-to-use-notifications.md).
- Declare the notification types that your app supports and the custom actions the user may perform when the system delivers those notifications. See [`Declaring your actionable notification types`](declaring-your-actionable-notification-types.md).
- Schedule the delivery of notifications from your app. See [`Scheduling a notification locally from your app`](scheduling-a-notification-locally-from-your-app.md).
- Process the payloads from remote notifications the system delivers by Apple Push Notification service (APNs). See [`Handling notifications and notification-related actions`](handling-notifications-and-notification-related-actions.md).
- Manage the already delivered notifications the system displays in Notification Center. See Managing Delivered Notifications.
- Handle user-selected actions associated with your custom notification types. See [`Handling notifications and notification-related actions`](handling-notifications-and-notification-related-actions.md).
- Get the notification-related settings for your app. See Managing Settings and Authorization.

To handle incoming notifications and notification-related actions, create an object that adopts the [`UNUserNotificationCenterDelegate`](unusernotificationcenterdelegate.md) protocol and assign it to the [`delegate`](unusernotificationcenter/delegate.md) property. Always assign an object to the [`delegate`](unusernotificationcenter/delegate.md) property before performing any tasks that might interact with that delegate.

You may use the shared user notification center object simultaneously from any of your app’s threads. The object processes requests serially in the order that the system initiates them.

## Topics

### Managing the notification center
- [class func current() -> UNUserNotificationCenter](unusernotificationcenter/current.md)
  Returns your app’s notification center.
- [func getNotificationSettings(completionHandler: (UNNotificationSettings) -> Void)](unusernotificationcenter/getnotificationsettings(completionhandler:).md)
  Retrieves the authorization and feature-related settings for your app.
- [func setBadgeCount(Int, withCompletionHandler: (((any Error)?) -> Void)?)](unusernotificationcenter/setbadgecount(_:withcompletionhandler:).md)
  Updates the badge count for your app’s icon.
### Requesting authorization
- [func requestAuthorization(options: UNAuthorizationOptions, completionHandler: (Bool, (any Error)?) -> Void)](unusernotificationcenter/requestauthorization(options:completionhandler:).md)
  Requests a person’s authorization to allow local and remote notifications for your app.
- [struct UNAuthorizationOptions](unauthorizationoptions.md)
  Options that determine the authorized features of local and remote notifications.
### Processing received notifications
- [var delegate: (any UNUserNotificationCenterDelegate)?](unusernotificationcenter/delegate.md)
  The notification center’s delegate.
- [protocol UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md)
  An interface for processing incoming notifications and responding to notification actions.
- [var supportsContentExtensions: Bool](unusernotificationcenter/supportscontentextensions.md)
  A Boolean value that indicates whether the device supports notification content extensions.
### Scheduling notifications
- [func add(UNNotificationRequest, withCompletionHandler: (((any Error)?) -> Void)?)](unusernotificationcenter/add(_:withcompletionhandler:).md)
  Schedules the delivery of a local notification.
- [func getPendingNotificationRequests(completionHandler: ([UNNotificationRequest]) -> Void)](unusernotificationcenter/getpendingnotificationrequests(completionhandler:).md)
  Fetches all of your app’s local notifications that are pending delivery.
- [func removePendingNotificationRequests(withIdentifiers: [String])](unusernotificationcenter/removependingnotificationrequests(withidentifiers:).md)
  Removes your app’s local notifications that are pending and match the specified identifiers.
- [func removeAllPendingNotificationRequests()](unusernotificationcenter/removeallpendingnotificationrequests.md)
  Removes all of your app’s pending local notifications.
### Removing delivered notifications
- [func getDeliveredNotifications(completionHandler: ([UNNotification]) -> Void)](unusernotificationcenter/getdeliverednotifications(completionhandler:).md)
  Fetches all of your app’s delivered notifications that are still present in Notification Center.
- [func removeDeliveredNotifications(withIdentifiers: [String])](unusernotificationcenter/removedeliverednotifications(withidentifiers:).md)
  Removes your app’s notifications from Notification Center that match the specified identifiers.
- [func removeAllDeliveredNotifications()](unusernotificationcenter/removealldeliverednotifications.md)
  Removes all of your app’s delivered notifications from Notification Center.
### Managing notification categories
- [func setNotificationCategories(Set<UNNotificationCategory>)](unusernotificationcenter/setnotificationcategories(_:).md)
  Registers the notification categories that your app supports.
- [func getNotificationCategories(completionHandler: (Set<UNNotificationCategory>) -> Void)](unusernotificationcenter/getnotificationcategories(completionhandler:).md)
  Fetches your app’s registered notification categories.
### Handling errors
- [struct UNError](unerror.md)
  An object that represents a notification error.
- [UNError.Code](unerror/code.md)
  Constants that identify notification errors.
- [let UNErrorDomain: String](unerrordomain.md)
  The error domain for notifications.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md)
  An interface for processing incoming notifications and responding to notification actions.
- [class UNNotificationSettings](unnotificationsettings.md)
  The object for managing notification-related settings and the authorization status of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter)*