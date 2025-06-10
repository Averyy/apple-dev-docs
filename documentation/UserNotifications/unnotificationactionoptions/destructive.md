# destructive

**Framework**: User Notifications  
**Kind**: property

The action performs a destructive task.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var destructive: UNNotificationActionOptions { get }
```

## Mentions

- [Declaring your actionable notification types](declaring-your-actionable-notification-types.md)

#### Discussion

Use this option for actions that delete user data or change the app irrevocably. The action button is displayed with special highlighting to indicate that it performs a destructive task.

## See Also

- [static var authenticationRequired: UNNotificationActionOptions](unnotificationactionoptions/authenticationrequired.md)
  The action can be performed only on an unlocked device.
- [static var foreground: UNNotificationActionOptions](unnotificationactionoptions/foreground.md)
  The action causes the app to launch in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions/destructive)*