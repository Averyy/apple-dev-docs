# sound

**Framework**: User Notifications  
**Kind**: property

The sound that plays when the system delivers the notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var sound: UNNotificationSound? { get }
```

#### Discussion

Notifications can play a default sound or a custom sound. For information on how to specify custom sounds for your notifications, see [`UNNotificationSound`](unnotificationsound.md).

## See Also

- [var interruptionLevel: UNNotificationInterruptionLevel](unnotificationcontent/interruptionlevel.md)
  The notification’s importance and required delivery timing.
- [enum UNNotificationInterruptionLevel](unnotificationinterruptionlevel.md)
  Constants that indicate the importance and delivery timing of a notification.
- [var relevanceScore: Double](unnotificationcontent/relevancescore.md)
  The score the system uses to determine if the notification is the summary’s featured notification.
- [var filterCriteria: String?](unnotificationcontent/filtercriteria.md)
  The criteria the system evaluates to determine if it displays the notification in the current Focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/sound)*