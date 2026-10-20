# sound

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

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
var sound: UNNotificationSound? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) UNNotificationSound * sound;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) UNNotificationSound * sound;
```

#### Discussion

Use this property to specify the sound that you want played when the notification arrives. If your app isn’t authorized to play sounds for notifications, the system ignores this property.

For information on how to specify sounds for your notifications, see [`UNNotificationSound`](../unnotificationsound.md).

## See Also

### Integrating with the system
- [var interruptionLevel: UNNotificationInterruptionLevel](./interruptionlevel.md)
  The notification’s importance and required delivery timing.
- [enum UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md)
  Constants that indicate the importance and delivery timing of a notification.
- [var relevanceScore: Double](./relevancescore.md)
  The score the system uses to determine if the notification is the summary’s featured notification.
- [var filterCriteria: String?](./filtercriteria.md)
  The criteria the system evaluates to determine if it displays the notification in the current Focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/sound)*