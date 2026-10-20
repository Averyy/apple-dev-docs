# icon

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The icon associated with the action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@NSCopying
var icon: UNNotificationActionIcon? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) UNNotificationActionIcon * icon;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) UNNotificationActionIcon * icon;
```

#### Discussion

The system displays this icon in the notification interface to help the user identify the app associated with the action.

## See Also

### Getting Information
- [var identifier: String](./identifier.md)
  The unique string that your app uses to identify the action.
- [var title: String](./title.md)
  The localized string to use as the title of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationaction/icon)*