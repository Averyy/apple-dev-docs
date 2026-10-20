# UNAuthorizationStatus.denied

**Framework**: User Notifications  
**Kind**: case  
**Role**: Case

The app isn’t authorized to schedule or receive notifications.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case denied
```

```c
UNAuthorizationStatusDenied
```

## See Also

### Status
- [UNAuthorizationStatus.notDetermined](./notdetermined.md)
  The user hasn’t yet made a choice about whether the app is allowed to schedule notifications.
- [UNAuthorizationStatus.authorized](./authorized.md)
  The app is authorized to schedule or receive notifications.
- [UNAuthorizationStatus.provisional](./provisional.md)
  The application is provisionally authorized to post noninterruptive user notifications.
- [UNAuthorizationStatus.ephemeral](./ephemeral.md)
  The app is authorized to schedule or receive notifications for a limited amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/denied)*