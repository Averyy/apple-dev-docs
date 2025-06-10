# UNNotificationInterruptionLevel.active

**Framework**: User Notifications  
**Kind**: case

The system presents the notification immediately, lights up the screen, and can play a sound.

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
case active
```

#### Discussion

This is the default interruption level. Active notifications won’t break through system notification controls.

## See Also

- [UNNotificationInterruptionLevel.critical](unnotificationinterruptionlevel/critical.md)
  The system presents the notification immediately, lights up the screen, and bypasses the mute switch to play a sound.
- [UNNotificationInterruptionLevel.passive](unnotificationinterruptionlevel/passive.md)
  The system adds the notification to the notification list without lighting up the screen or playing a sound.
- [UNNotificationInterruptionLevel.timeSensitive](unnotificationinterruptionlevel/timesensitive.md)
  The system presents the notification immediately, lights up the screen, can play a sound, and breaks through system notification controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active)*