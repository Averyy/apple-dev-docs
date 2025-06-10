# init(dateMatching:repeats:)

**Framework**: User Notifications  
**Kind**: init

Creates a calendar trigger using the date components parameter.

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
convenience init(dateMatching dateComponents: DateComponents, repeats: Bool)
```

#### Return Value

A new calendar trigger based on the specified temporal information.

#### Discussion

If you specify `true` for the `repeats` parameter, you must explicitly remove the notification request to stop the delivery of the associated notification. Use the methods of [`UNUserNotificationCenter`](unusernotificationcenter.md) to remove notification requests that are no longer needed.

## Parameters

- `dateComponents`: The temporal information to use when constructing the trigger. Provide only the date components that are relevant for your trigger.
- `repeats`: Specify   to deliver the notification one time. Specify   to reschedule the notification request each time the system delivers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger/init(datematching:repeats:))*