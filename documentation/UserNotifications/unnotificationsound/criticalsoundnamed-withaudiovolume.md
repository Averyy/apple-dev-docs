# criticalSoundNamed(_:withAudioVolume:)

**Framework**: User Notifications  
**Kind**: method

Creates a custom sound object for critical alerts with the volume you specify.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
class func criticalSoundNamed(_ name: UNNotificationSoundName, withAudioVolume volume: Float) -> Self
```

#### Return Value

A sound object representing a custom critical alert sound at the specified volume.

#### Discussion

Critical alerts ignore the mute switch and Do Not Disturb. They require a special entitlement issued by Apple.

## Parameters

- `name`: The name of the sound file to play. This file must be located in the current executable’s main bundle or in the   directory of the current app container directory. If files exist at both locations, the system uses the file from the   directory. This parameter must not be  .
- `volume`: The volume must be a value between 0.0 and 1.0.

## See Also

- [class var defaultCritical: UNNotificationSound](unnotificationsound/defaultcritical.md)
  The default sound used for critical alerts.
- [class func defaultCriticalSound(withAudioVolume: Float) -> Self](unnotificationsound/defaultcriticalsound(withaudiovolume:).md)
  Creates a sound object that plays the default critical alert sound at the volume you specify.
- [class func criticalSoundNamed(UNNotificationSoundName) -> Self](unnotificationsound/criticalsoundnamed(_:).md)
  Creates a custom sound object for critical alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsound/criticalsoundnamed(_:withaudiovolume:))*