# repeats

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the system reschedules the notification after it’s delivered.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var repeats: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) BOOL repeats;
```

*macOS*

```objc
@property (atomic, readonly) BOOL repeats;
```

#### Discussion

When this property is [`false`](../../Swift/false.md), the system delivers the notification only once. When this property is [`true`](../../Swift/true.md), the system reschedules the notification request automatically, resulting in the system delivering the notification each time the trigger condition is met. To unschedule the notification request, use the methods of the [`UNUserNotificationCenter`](../unusernotificationcenter.md) to remove the notification request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationtrigger/repeats)*