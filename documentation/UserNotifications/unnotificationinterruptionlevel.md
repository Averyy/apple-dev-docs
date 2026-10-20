# UNNotificationInterruptionLevel

**Framework**: User Notifications  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the importance and delivery timing of a notification.

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
enum UNNotificationInterruptionLevel
```

```c
enum UNNotificationInterruptionLevel : NSUInteger;
```

## Mentions

- [Generating a remote notification](./generating-a-remote-notification.md)

## Topics

### Enumeration Cases
- [UNNotificationInterruptionLevel.active](./unnotificationinterruptionlevel/active.md)
  The system presents the notification immediately, lights up the screen, and can play a sound.
- [UNNotificationInterruptionLevel.critical](./unnotificationinterruptionlevel/critical.md)
  The system presents the notification immediately, lights up the screen, and bypasses the mute switch to play a sound.
- [UNNotificationInterruptionLevel.passive](./unnotificationinterruptionlevel/passive.md)
  The system adds the notification to the notification list without lighting up the screen or playing a sound.
- [UNNotificationInterruptionLevel.timeSensitive](./unnotificationinterruptionlevel/timesensitive.md)
  The system presents the notification immediately, lights up the screen, can play a sound, and breaks through system notification controls.
### Initializers
- [init?(rawValue: UInt)](./unnotificationinterruptionlevel/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Integrating with the system
- [var sound: UNNotificationSound?](./unmutablenotificationcontent/sound.md)
  The sound that plays when the system delivers the notification.
- [var interruptionLevel: UNNotificationInterruptionLevel](./unmutablenotificationcontent/interruptionlevel.md)
  The notification’s importance and required delivery timing.
- [var relevanceScore: Double](./unmutablenotificationcontent/relevancescore.md)
  The score the system uses to determine if the notification is the summary’s featured notification.
- [var filterCriteria: String?](./unmutablenotificationcontent/filtercriteria.md)
  The criteria the system evaluates to determine if it displays the notification in the current Focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel)*