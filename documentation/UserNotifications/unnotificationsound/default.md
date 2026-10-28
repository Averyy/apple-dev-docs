# default

**Framework**: User Notifications  
**Kind**: property  
**Role**: Type Property

Returns an object representing the default sound for notifications.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
class var `default`: UNNotificationSound { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (class, nonatomic, copy, readonly) UNNotificationSound * defaultSound;
```

*macOS*

```objc
@property (class, atomic, copy, readonly) UNNotificationSound * defaultSound;
```

## Return Value

A sound object that represents the default notification sound.

## See Also

### Creating Notification Sounds
- [convenience init(named: UNNotificationSoundName)](./init%28named%29.md)
  Creates a sound object that represents a custom sound file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsound/default)*