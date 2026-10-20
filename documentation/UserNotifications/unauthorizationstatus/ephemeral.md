# UNAuthorizationStatus.ephemeral

**Framework**: User Notifications  
**Kind**: case  
**Role**: Case

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

```c
UNAuthorizationStatusEphemeral
```

#### Discussion

An App Clip may have the ability to schedule or receive notifications for a limited amount of time. For more information, see [Enabling notifications in App Clips](../../AppClip/enabling-notifications-in-app-clips.md).

## See Also

### Status
- [UNAuthorizationStatus.notDetermined](./notdetermined.md)
  The user hasn’t yet made a choice about whether the app is allowed to schedule notifications.
- [UNAuthorizationStatus.denied](./denied.md)
  The app isn’t authorized to schedule or receive notifications.
- [UNAuthorizationStatus.authorized](./authorized.md)
  The app is authorized to schedule or receive notifications.
- [UNAuthorizationStatus.provisional](./provisional.md)
  The application is provisionally authorized to post noninterruptive user notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/ephemeral)*