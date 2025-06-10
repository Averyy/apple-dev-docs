# defaultCriticalSound(withAudioVolume:)

**Framework**: User Notifications  
**Kind**: method

Creates a sound object that plays the default critical alert sound at the volume you specify.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class func defaultCriticalSound(withAudioVolume volume: Float) -> Self
```

#### Return Value

A sound object representing the default critical alert sound at the specified volume.

#### Discussion

Critical alerts ignore the mute switch and Do Not Disturb. They require a special entitlement issued by Apple.

## Parameters

- `volume`: The volume must be a value between 0.0 and 1.0.

## See Also

- [class var defaultCritical: UNNotificationSound](unnotificationsound/defaultcritical.md)
  The default sound used for critical alerts.
- [class func criticalSoundNamed(UNNotificationSoundName) -> Self](unnotificationsound/criticalsoundnamed(_:).md)
  Creates a custom sound object for critical alerts.
- [class func criticalSoundNamed(UNNotificationSoundName, withAudioVolume: Float) -> Self](unnotificationsound/criticalsoundnamed(_:withaudiovolume:).md)
  Creates a custom sound object for critical alerts with the volume you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsound/defaultcriticalsound(withaudiovolume:))*