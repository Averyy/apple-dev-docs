# UNNotificationSettings

**Framework**: Usernotifications  
**Kind**: class

The object for managing notification-related settings and the authorization status of your app.

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
class UNNotificationSettings
```

## Mentions

- [Asking permission to use notifications](asking-permission-to-use-notifications.md)

#### Overview

A [`UNNotificationSettings`](unnotificationsettings.md) object contains the current authorization status and notification-related settings for your app. Apps must receive authorization to schedule notifications and to interact with the user. Apps that run in CarPlay must similarly receive authorization to do so. Use this object to determine what notification-related actions your app can perform. You might then use that information to enable, disable, or adjust your app’s notification-related behaviors. Regardless of whether you take action, the system enforces your app’s settings by preventing denied interactions from occurring.

You don’t create instances of this class directly. Instead, call the [`getNotificationSettings(completionHandler:)`](unusernotificationcenter/getnotificationsettings(completionhandler:).md) method of your app’s [`UNUserNotificationCenter`](unusernotificationcenter.md) object to get the current settings.

For more information about requesting authorization for user interactions, see [`UNUserNotificationCenter`](unusernotificationcenter.md).

## Topics

### Getting the Authorization Status
- [var authorizationStatus: UNAuthorizationStatus](unnotificationsettings/authorizationstatus.md)
  The app’s ability to schedule and receive local and remote notifications.
- [enum UNAuthorizationStatus](unauthorizationstatus.md)
  Constants indicating whether the app is allowed to schedule notifications.
### Getting Device-Specific Settings
- [var notificationCenterSetting: UNNotificationSetting](unnotificationsettings/notificationcentersetting.md)
  The setting that indicates whether your app’s notifications appear in Notification Center.
- [var lockScreenSetting: UNNotificationSetting](unnotificationsettings/lockscreensetting.md)
  The setting that indicates whether your app’s notifications appear on a device’s Lock screen.
- [var carPlaySetting: UNNotificationSetting](unnotificationsettings/carplaysetting.md)
  The setting that indicates whether your app’s notifications appear in CarPlay.
- [var alertSetting: UNNotificationSetting](unnotificationsettings/alertsetting.md)
  The authorization status for displaying alerts.
- [var badgeSetting: UNNotificationSetting](unnotificationsettings/badgesetting.md)
  The setting that indicates whether badges appear on your app’s icon.
- [var soundSetting: UNNotificationSetting](unnotificationsettings/soundsetting.md)
  The authorization status for playing sounds for incoming notifications.
- [var criticalAlertSetting: UNNotificationSetting](unnotificationsettings/criticalalertsetting.md)
  The authorization status for playing sounds for critical alerts.
- [var announcementSetting: UNNotificationSetting](unnotificationsettings/announcementsetting.md)
  The setting that indicates whether Siri can announce your app’s notifications.
- [var scheduledDeliverySetting: UNNotificationSetting](unnotificationsettings/scheduleddeliverysetting.md)
  The setting that indicates the system schedules the notification.
- [var timeSensitiveSetting: UNNotificationSetting](unnotificationsettings/timesensitivesetting.md)
  The setting that indicates the system treats the notification as time-sensitive.
- [enum UNNotificationSetting](unnotificationsetting.md)
  Constants that indicate the current status of a notification setting.
### Getting Interface Settings
- [var alertStyle: UNAlertStyle](unnotificationsettings/alertstyle.md)
  The type of alert that the app may display when the device is unlocked.
- [enum UNAlertStyle](unalertstyle.md)
  Constants indicating the presentation styles for alerts.
- [var showPreviewsSetting: UNShowPreviewsSetting](unnotificationsettings/showpreviewssetting.md)
  The setting that indicates whether the app shows a preview of the notification’s content.
- [enum UNShowPreviewsSetting](unshowpreviewssetting.md)
  Constants indicating the style previewing a notification’s content.
- [var providesAppNotificationSettings: Bool](unnotificationsettings/providesappnotificationsettings.md)
  A Boolean value indicating the system displays a button for in-app notification settings.
### Instance Properties
- [var directMessagesSetting: UNNotificationSetting](unnotificationsettings/directmessagessetting.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class UNUserNotificationCenter](unusernotificationcenter.md)
  The central object for managing notification-related activities for your app or app extension.
- [protocol UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md)
  An interface for processing incoming notifications and responding to notification actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings)*