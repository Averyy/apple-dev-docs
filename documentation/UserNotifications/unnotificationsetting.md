# UNNotificationSetting

**Framework**: User Notifications  
**Kind**: enum

Constants that indicate the current status of a notification setting.

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
enum UNNotificationSetting
```

## Topics

### Constants
- [UNNotificationSetting.notSupported](unnotificationsetting/notsupported.md)
  The setting is not available to your app.
- [UNNotificationSetting.disabled](unnotificationsetting/disabled.md)
  The setting is disabled.
- [UNNotificationSetting.enabled](unnotificationsetting/enabled.md)
  The setting is enabled.
### Initializers
- [init?(rawValue: Int)](unnotificationsetting/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsetting)*