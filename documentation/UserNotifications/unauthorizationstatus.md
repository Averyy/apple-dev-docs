# UNAuthorizationStatus

**Framework**: User Notifications  
**Kind**: enum  
**Role**: Enumeration

Constants indicating whether the app is allowed to schedule notifications.

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
enum UNAuthorizationStatus
```

```c
enum UNAuthorizationStatus : NSInteger;
```

## Topics

### Status
- [UNAuthorizationStatus.notDetermined](./unauthorizationstatus/notdetermined.md)
  The user hasn’t yet made a choice about whether the app is allowed to schedule notifications.
- [UNAuthorizationStatus.denied](./unauthorizationstatus/denied.md)
  The app isn’t authorized to schedule or receive notifications.
- [UNAuthorizationStatus.authorized](./unauthorizationstatus/authorized.md)
  The app is authorized to schedule or receive notifications.
- [UNAuthorizationStatus.provisional](./unauthorizationstatus/provisional.md)
  The application is provisionally authorized to post noninterruptive user notifications.
- [UNAuthorizationStatus.ephemeral](./unauthorizationstatus/ephemeral.md)
  The app is authorized to schedule or receive notifications for a limited amount of time.
### Initializers
- [init?(rawValue: Int)](./unauthorizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Authorization Status
- [var authorizationStatus: UNAuthorizationStatus](./unnotificationsettings/authorizationstatus.md)
  The app’s ability to schedule and receive local and remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unauthorizationstatus)*