# criticalAlertSetting

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The authorization status for playing sounds for critical alerts.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var criticalAlertSetting: UNNotificationSetting { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) UNNotificationSetting criticalAlertSetting;
```

*macOS*

```objc
@property (atomic, readonly) UNNotificationSetting criticalAlertSetting;
```

#### Discussion

When [`UNNotificationSetting.enabled`](../unnotificationsetting/enabled.md), this property authorizes the app to play critical sounds that ignore Do Not Disturb and the device’s mute switch.

For local notifications, the system attempts to play a critical sound when the [`sound`](../unnotificationcontent/sound.md) property of the [`UNNotificationContent`](../unnotificationcontent.md) object contains an object returned by the [`defaultCritical`](../unnotificationsound/defaultcritical.md) property, the [`criticalSoundNamed(_:)`](../unnotificationsound/criticalsoundnamed%28_%29.md) method, or a related method.

For remote notifications, the system attempts to play a critical sound when the notification’s payload contains a `sound` directory that contains the `critical` key.

Critical alerts require a special entitlement issued by Apple.

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
- [var badgeSetting: UNNotificationSetting](./badgesetting.md)
  The setting that indicates whether badges appear on your app’s icon.
- [var soundSetting: UNNotificationSetting](./soundsetting.md)
  The authorization status for playing sounds for incoming notifications.
- [var announcementSetting: UNNotificationSetting](./announcementsetting.md)
  The setting that indicates whether Siri can announce your app’s notifications.
- [var scheduledDeliverySetting: UNNotificationSetting](./scheduleddeliverysetting.md)
  The setting that indicates the system schedules the notification.
- [var timeSensitiveSetting: UNNotificationSetting](./timesensitivesetting.md)
  The setting that indicates the system treats the notification as time-sensitive.
- [enum UNNotificationSetting](../unnotificationsetting.md)
  Constants that indicate the current status of a notification setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/criticalalertsetting)*