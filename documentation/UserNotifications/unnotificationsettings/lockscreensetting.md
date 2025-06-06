# lockScreenSetting

**Framework**: Usernotifications  
**Kind**: property

The setting that indicates whether your app’s notifications appear on a device’s Lock screen.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var lockScreenSetting: UNNotificationSetting { get }
```

#### Discussion

Even if the user disables lock screen notifications, your notifications may still appear onscreen when the device is unlocked.

## See Also

- [var notificationCenterSetting: UNNotificationSetting](unnotificationsettings/notificationcentersetting.md)
  The setting that indicates whether your app’s notifications appear in Notification Center.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/lockscreensetting)*