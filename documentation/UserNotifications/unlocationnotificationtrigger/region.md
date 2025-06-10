# region

**Framework**: User Notifications  
**Kind**: property

The region used to determine when the system sends the notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var region: CLRegion { get }
```

#### Discussion

Use the [`notifyOnEntry`](https://developer.apple.com/documentation/CoreLocation/CLRegion/notifyOnEntry) and [`notifyOnExit`](https://developer.apple.com/documentation/CoreLocation/CLRegion/notifyOnExit) properties of this region to specify whether the system sends notifications when the user enters or exits the specified geographic area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger/region)*