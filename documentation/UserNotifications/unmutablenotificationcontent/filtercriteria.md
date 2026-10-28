# filterCriteria

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * filterCriteria;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * filterCriteria;
```

## Discussion

For more information, see [`SetFocusFilterIntent`](../../AppIntents/setfocusfilterintent.md).

## See Also

### Integrating with the system
- [var sound: UNNotificationSound?](./sound.md)
  The sound that plays when the system delivers the notification.
- [var interruptionLevel: UNNotificationInterruptionLevel](./interruptionlevel.md)
  The notification’s importance and required delivery timing.
- [enum UNNotificationInterruptionLevel](../unnotificationinterruptionlevel.md)
  Constants that indicate the importance and delivery timing of a notification.
- [var relevanceScore: Double](./relevancescore.md)
  The score the system uses to determine if the notification is the summary’s featured notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/filtercriteria)*