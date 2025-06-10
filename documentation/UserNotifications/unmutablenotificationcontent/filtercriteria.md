# filterCriteria

**Framework**: User Notifications  
**Kind**: property

The criteria the system evaluates to determine if it displays the notification in the current Focus.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var filterCriteria: String? { get set }
```

#### Discussion

For more information, see [`SetFocusFilterIntent`](https://developer.apple.com/documentation/AppIntents/SetFocusFilterIntent).

## See Also

- [var sound: UNNotificationSound?](unmutablenotificationcontent/sound.md)
  The sound that plays when the system delivers the notification.
- [var interruptionLevel: UNNotificationInterruptionLevel](unmutablenotificationcontent/interruptionlevel.md)
  The notification’s importance and required delivery timing.
- [enum UNNotificationInterruptionLevel](unnotificationinterruptionlevel.md)
  Constants that indicate the importance and delivery timing of a notification.
- [var relevanceScore: Double](unmutablenotificationcontent/relevancescore.md)
  The score the system uses to determine if the notification is the summary’s featured notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/filtercriteria)*