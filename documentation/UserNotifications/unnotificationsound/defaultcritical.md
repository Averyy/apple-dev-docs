# defaultCritical

**Framework**: User Notifications  
**Kind**: property  
**Role**: Type Property

The default sound used for critical alerts.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
class var defaultCritical: UNNotificationSound { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (class, nonatomic, copy, readonly) UNNotificationSound * defaultCriticalSound;
```

*macOS*

```objc
@property (class, atomic, copy, readonly) UNNotificationSound * defaultCriticalSound;
```

#### Discussion

Critical alerts ingore the mute switch and Do Not Disturb. They require a special entitlement issued by Apple.

## See Also

### Getting Critical Sounds
- [class func defaultCriticalSound(withAudioVolume: Float) -> Self](./defaultcriticalsound%28withaudiovolume%29.md)
  Creates a sound object that plays the default critical alert sound at the volume you specify.
- [class func criticalSoundNamed(UNNotificationSoundName) -> Self](./criticalsoundnamed%28_%29.md)
  Creates a custom sound object for critical alerts.
- [class func criticalSoundNamed(UNNotificationSoundName, withAudioVolume: Float) -> Self](./criticalsoundnamed%28_,withaudiovolume%29.md)
  Creates a custom sound object for critical alerts with the volume you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsound/defaultcritical)*