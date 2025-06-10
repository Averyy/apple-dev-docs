# UNNotificationInterruptionLevel.critical

**Framework**: User Notifications  
**Kind**: case

The system presents the notification immediately, lights up the screen, and bypasses the mute switch to play a sound.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case critical
```

#### Discussion

This interruption level requires an approved entitlement. The system always presents this notification, even when Do Not Disturb is active. If your app doesn’t assign a sound to this notification, the system uses the default critical alert sound.

## See Also

- [UNNotificationInterruptionLevel.active](unnotificationinterruptionlevel/active.md)
  The system presents the notification immediately, lights up the screen, and can play a sound.
- [UNNotificationInterruptionLevel.passive](unnotificationinterruptionlevel/passive.md)
  The system adds the notification to the notification list without lighting up the screen or playing a sound.
- [UNNotificationInterruptionLevel.timeSensitive](unnotificationinterruptionlevel/timesensitive.md)
  The system presents the notification immediately, lights up the screen, can play a sound, and breaks through system notification controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)*