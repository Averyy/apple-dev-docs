# badge

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The app accepts notifications that badge the app icon.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`requestAuthorization(options:completionHandler:)`](../../UserNotifications/unusernotificationcenter/requestauthorization%28options,completionhandler%29.md) and [`setNotificationCategories(_:)`](../../UserNotifications/unusernotificationcenter/setnotificationcategories%28_%29.md) instead.

## Declaration

```swift
static var badge: UIRemoteNotificationType { get }
```

```c
UIRemoteNotificationTypeBadge
```

## See Also

### Constants
- [static var sound: UIRemoteNotificationType](./sound.md)
  The app accepts alert sounds as notifications.
- [static var alert: UIRemoteNotificationType](./alert.md)
  The app accepts alert messages as notifications.
- [static var newsstandContentAvailability: UIRemoteNotificationType](./newsstandcontentavailability.md)
  The app accepts notifications that start the downloading of issue assets for Newsstand apps.
- [UIRemoteNotificationTypeNone](./uiremotenotificationtypenone.md)
  The app accepts no notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiremotenotificationtype/badge)*