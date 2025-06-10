# foreground

**Framework**: User Notifications  
**Kind**: property

The action causes the app to launch in the foreground.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var foreground: UNNotificationActionOptions { get }
```

#### Discussion

When the user selects an action containing this option, the system brings the app to the foreground, asking the user to unlock the device as needed. Use this option for actions that require the user to interact further with your app. Do not use this option simply to bring your app to the foreground.

## See Also

- [static var authenticationRequired: UNNotificationActionOptions](unnotificationactionoptions/authenticationrequired.md)
  The action can be performed only on an unlocked device.
- [static var destructive: UNNotificationActionOptions](unnotificationactionoptions/destructive.md)
  The action performs a destructive task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions/foreground)*