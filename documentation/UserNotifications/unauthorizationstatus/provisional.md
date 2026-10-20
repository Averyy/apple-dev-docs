# UNAuthorizationStatus.provisional

**Framework**: User Notifications  
**Kind**: case  
**Role**: Case

The application is provisionally authorized to post noninterruptive user notifications.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case provisional
```

```c
UNAuthorizationStatusProvisional
```

## Mentions

- [Asking permission to use notifications](../asking-permission-to-use-notifications.md)

## See Also

### Status
- [UNAuthorizationStatus.notDetermined](./notdetermined.md)
  The user hasn’t yet made a choice about whether the app is allowed to schedule notifications.
- [UNAuthorizationStatus.denied](./denied.md)
  The app isn’t authorized to schedule or receive notifications.
- [UNAuthorizationStatus.authorized](./authorized.md)
  The app is authorized to schedule or receive notifications.
- [UNAuthorizationStatus.ephemeral](./ephemeral.md)
  The app is authorized to schedule or receive notifications for a limited amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus/provisional)*