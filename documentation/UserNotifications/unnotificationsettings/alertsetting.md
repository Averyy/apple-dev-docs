# alertSetting

**Framework**: User Notifications  
**Kind**: property

The authorization status for displaying alerts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var alertSetting: UNNotificationSetting { get }
```

#### Discussion

When the value of this property is [`UNNotificationSetting.enabled`](unnotificationsetting/enabled.md), the app is authorized to display alerts. Authorization does not guarantee that alerts always appear on the user’s screen. When a device is unlocked, the [`alertStyle`](unnotificationsettings/alertstyle.md) property determines the presentation style for the alert, which can include not displaying the alert at all.

The system tries to display an alert when the [`title`](unnotificationcontent/title.md), [`subtitle`](unnotificationcontent/subtitle.md), or [`body`](unnotificationcontent/body.md) properties of a [`UNNotificationContent`](unnotificationcontent.md) object contain values, or when the `aps` dictionary in a remote notification contains the `alert` key.

## See Also

- [var notificationCenterSetting: UNNotificationSetting](unnotificationsettings/notificationcentersetting.md)
  The setting that indicates whether your app’s notifications appear in Notification Center.
- [var lockScreenSetting: UNNotificationSetting](unnotificationsettings/lockscreensetting.md)
  The setting that indicates whether your app’s notifications appear on a device’s Lock screen.
- [var carPlaySetting: UNNotificationSetting](unnotificationsettings/carplaysetting.md)
  The setting that indicates whether your app’s notifications appear in CarPlay.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/alertsetting)*