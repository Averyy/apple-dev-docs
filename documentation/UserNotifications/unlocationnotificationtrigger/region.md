# region

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The region used to determine when the system sends the notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var region: CLRegion { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) CLRegion * region;
```

*macOS*

```objc
@property (atomic, copy, readonly) CLRegion * region;
```

#### Discussion

Use the [`notifyOnEntry`](../../CoreLocation/clregion/notifyonentry.md) and [`notifyOnExit`](../../CoreLocation/clregion/notifyonexit.md) properties of this region to specify whether the system sends notifications when the user enters or exits the specified geographic area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger/region)*