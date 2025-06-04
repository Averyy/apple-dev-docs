# isRegisteredForRemoteNotifications

**Framework**: Watchkit  
**Kind**: property

A Boolean value that indicates if the app has successfully registered for remote notifications.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor var isRegisteredForRemoteNotifications: Bool { get }
```

## Overview

This method indicates whether your app successfully registered for remote notifications using the [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/watchkit/wkextension/registerforremotenotifications()) method. It also takes into account the notification permissions set by the user. It does not give any indication about whether remote notifications are available.

## See Also

- [func registerForRemoteNotifications()](registerforremotenotifications().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/registerforremotenotifications()))
- [func unregisterForRemoteNotifications()](unregisterforremotenotifications().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/unregisterforremotenotifications()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isregisteredforremotenotifications)*