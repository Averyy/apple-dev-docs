# init(region:repeats:)

**Framework**: User Notifications  
**Kind**: init  
**Role**: Initializer

Creates a location trigger using the region parameter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(region: CLRegion, repeats: Bool)
```

```objc
+ (instancetype) triggerWithRegion:(CLRegion *) region repeats:(BOOL) repeats;
```

#### Return Value

A new location trigger object with the specified region.

#### Discussion

If you specify `true` for the `repeats` parameter, you must explicitly remove the notification request to stop the delivery of the associated notification. Use the methods of [`UNUserNotificationCenter`](../unusernotificationcenter.md) to remove notification requests that are no longer needed.

## Parameters

- `region`: The geographic region that must be entered or exited. Use the region object to specify whether to deliver notifications on entry, on exit, or both.
- `repeats`: Specify [`false`](../../Swift/false.md) to deliver the notification one time. Specify [`true`](../../Swift/true.md) to reschedule the notification request each time the system delivers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger/init(region:repeats:))*