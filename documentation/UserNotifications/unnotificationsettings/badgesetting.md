# badgeSetting

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The setting that indicates whether badges appear on your app’s icon.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var badgeSetting: UNNotificationSetting { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) UNNotificationSetting badgeSetting;
```

*macOS*

```objc
@property (atomic, readonly) UNNotificationSetting badgeSetting;
```

## Discussion

When the value of this property is [`UNNotificationSetting.enabled`](../unnotificationsetting/enabled.md), the app is authorized to badge its icon. The system tries to badge your app’s icon when the [`badge`](../unnotificationcontent/badge.md) property of a [`UNNotificationContent`](../unnotificationcontent.md) object contain a value, or when the `aps` dictionary in a remote notification contains the `badge` key.

## See Also

### Getting Device-Specific Settings
- [var notificationCenterSetting: UNNotificationSetting](./notificationcentersetting.md)
  The setting that indicates whether your app’s notifications appear in Notification Center.
- [var lockScreenSetting: UNNotificationSetting](./lockscreensetting.md)
  The setting that indicates whether your app’s notifications appear on a device’s Lock screen.
- [var carPlaySetting: UNNotificationSetting](./carplaysetting.md)
  The setting that indicates whether your app’s notifications appear in CarPlay.
- [var alertSetting: UNNotificationSetting](./alertsetting.md)
  The authorization status for displaying alerts.
- [var soundSetting: UNNotificationSetting](./soundsetting.md)
  The authorization status for playing sounds for incoming notifications.
- [var criticalAlertSetting: UNNotificationSetting](./criticalalertsetting.md)
  The authorization status for playing sounds for critical alerts.
- [var announcementSetting: UNNotificationSetting](./announcementsetting.md)
  The setting that indicates whether Siri can announce your app’s notifications.
- [var scheduledDeliverySetting: UNNotificationSetting](./scheduleddeliverysetting.md)
  The setting that indicates the system schedules the notification.
- [var timeSensitiveSetting: UNNotificationSetting](./timesensitivesetting.md)
  The setting that indicates the system treats the notification as time-sensitive.
- [enum UNNotificationSetting](../unnotificationsetting.md)
  Constants that indicate the current status of a notification setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/badgesetting)*