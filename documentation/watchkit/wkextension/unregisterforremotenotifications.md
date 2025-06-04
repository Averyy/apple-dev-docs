# unregisterForRemoteNotifications()

**Framework**: Watchkit  
**Kind**: method

Unregister for all remote notifications received from Apple Push Notification service (APNs).

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor func unregisterForRemoteNotifications()
```

## Overview

Use this method to unregister from all remote notifications; for example, unregister to stop receiving notifications when the user logs out of their account.

## See Also

- @MainActor func registerForRemoteNotifications() ([Apple Docs](https://developer.apple.com/documentation/UIKit/UIApplication/registerForRemoteNotifications()))
- [func registerForRemoteNotifications()](registerforremotenotifications().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/registerforremotenotifications()))
- [var isRegisteredForRemoteNotifications: Bool](isregisteredforremotenotifications.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isregisteredforremotenotifications))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/unregisterforremotenotifications())*