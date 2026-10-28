# relevanceScore

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The score the system uses to determine if the notification is the summary’s featured notification.

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
var relevanceScore: Double { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readwrite) double relevanceScore;
```

*macOS*

```objc
@property (atomic, assign, readwrite) double relevanceScore;
```

## Discussion

The system uses the `relevanceScore`, a value between `0` and `1`, to sort the notifications from your app. The highest score gets featured in the notification summary.

## See Also

### Integrating with the system
- [var sound: UNNotificationSound?](./sound.md)
  The sound that plays when the system delivers the notification.
- [var interruptionLevel: UNNotificationInterruptionLevel](./interruptionlevel.md)
  The notification’s importance and required delivery timing.
- [enum UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md)
  Constants that indicate the importance and delivery timing of a notification.
- [var filterCriteria: String?](./filtercriteria.md)
  The criteria the system evaluates to determine if it displays the notification in the current Focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/relevancescore)*