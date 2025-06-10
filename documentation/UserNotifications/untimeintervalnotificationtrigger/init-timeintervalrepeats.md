# init(timeInterval:repeats:)

**Framework**: User Notifications  
**Kind**: init

Creates a time interval trigger using the time value parameter.

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
convenience init(timeInterval: TimeInterval, repeats: Bool)
```

#### Return Value

A new time interval trigger based on the specified temporal information.

#### Discussion

If you specify `true` for the `repeats` parameter, you must explicitly remove the notification request to stop the delivery of the associated notification. Use the methods of [`UNUserNotificationCenter`](unusernotificationcenter.md) to remove notification requests that are no longer needed.

## Parameters

- `timeInterval`: The time (in seconds) that must elapse from the current time before the trigger fires. This value must be greater than zero.
- `repeats`: Specify   to deliver the notification one time. Specify   to reschedule the notification request each time the system delivers the notification. If this parameter is  , the value in the   parameter must be 60 seconds or greater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger/init(timeinterval:repeats:))*