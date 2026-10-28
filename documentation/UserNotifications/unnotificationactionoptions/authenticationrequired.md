# authenticationRequired

**Framework**: User Notifications  
**Kind**: property  
**Role**: Type Property

The action can be performed only on an unlocked device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var authenticationRequired: UNNotificationActionOptions { get }
```

```c
UNNotificationActionOptionAuthenticationRequired
```

## Discussion

When the user selects an action with this option, the system prompts the user to unlock the device. After unlocking, the system notifies your app of the selected action. You might use option to perform actions that require accessing data that is encrypted while the device is locked.

## See Also

### Constants
- [static var destructive: UNNotificationActionOptions](./destructive.md)
  The action performs a destructive task.
- [static var foreground: UNNotificationActionOptions](./foreground.md)
  The action causes the app to launch in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions/authenticationrequired)*