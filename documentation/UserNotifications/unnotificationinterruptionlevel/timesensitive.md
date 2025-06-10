# UNNotificationInterruptionLevel.timeSensitive

**Framework**: User Notifications  
**Kind**: case

The system presents the notification immediately, lights up the screen, can play a sound, and breaks through system notification controls.

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
case timeSensitive
```

#### Discussion

Time Sensitive notifications are similar to active notifications, but can break through system controls such as Notification Summary and Focus. The user can turn off the ability for time sensitive notification interruptions.

## See Also

- [UNNotificationInterruptionLevel.active](unnotificationinterruptionlevel/active.md)
  The system presents the notification immediately, lights up the screen, and can play a sound.
- [UNNotificationInterruptionLevel.critical](unnotificationinterruptionlevel/critical.md)
  The system presents the notification immediately, lights up the screen, and bypasses the mute switch to play a sound.
- [UNNotificationInterruptionLevel.passive](unnotificationinterruptionlevel/passive.md)
  The system adds the notification to the notification list without lighting up the screen or playing a sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)*