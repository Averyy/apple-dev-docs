# interruptionLevel

**Framework**: User Notifications  
**Kind**: property

The notification’s importance and required delivery timing.

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
var interruptionLevel: UNNotificationInterruptionLevel { get set }
```

## See Also

- [var sound: UNNotificationSound?](unmutablenotificationcontent/sound.md)
  The sound that plays when the system delivers the notification.
- [enum UNNotificationInterruptionLevel](unnotificationinterruptionlevel.md)
  Constants that indicate the importance and delivery timing of a notification.
- [var relevanceScore: Double](unmutablenotificationcontent/relevancescore.md)
  The score the system uses to determine if the notification is the summary’s featured notification.
- [var filterCriteria: String?](unmutablenotificationcontent/filtercriteria.md)
  The criteria the system evaluates to determine if it displays the notification in the current Focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/interruptionlevel)*