# userNotificationCenter(_:openSettingsFor:)

**Framework**: User Notifications  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to display the in-app notification settings.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
optional func userNotificationCenter(_ center: UNUserNotificationCenter, openSettingsFor notification: UNNotification?)
```

```objc
- (void) userNotificationCenter:(UNUserNotificationCenter *) center openSettingsForNotification:(UNNotification *) notification;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/usernotificationcenter(_:opensettingsfor:))*