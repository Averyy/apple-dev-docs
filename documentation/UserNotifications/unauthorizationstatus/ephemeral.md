# UNAuthorizationStatus.ephemeral

**Framework**: User Notifications  
**Kind**: case

The app is authorized to schedule or receive notifications for a limited amount of time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
case ephemeral
```

#### Discussion

An App Clip may have the ability to schedule or receive notifications for a limited amount of time. For more information, see [`Enabling notifications in App Clips`](https://developer.apple.com/documentation/AppClip/enabling-notifications-in-app-clips).

## See Also

- [UNAuthorizationStatus.notDetermined](unauthorizationstatus/notdetermined.md)
  The user hasn’t yet made a choice about whether the app is allowed to schedule notifications.
- [UNAuthorizationStatus.denied](unauthorizationstatus/denied.md)
  The app isn’t authorized to schedule or receive notifications.
- [UNAuthorizationStatus.authorized](unauthorizationstatus/authorized.md)
  The app is authorized to schedule or receive notifications.
- [UNAuthorizationStatus.provisional](unauthorizationstatus/provisional.md)
  The application is provisionally authorized to post noninterruptive user notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/ephemeral)*