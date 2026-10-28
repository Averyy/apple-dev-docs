# criticalSoundNamed(_:)

**Framework**: User Notifications  
**Kind**: method  
**Role**: Type Method

Creates a custom sound object for critical alerts.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
class func criticalSoundNamed(_ name: UNNotificationSoundName) -> Self
```

```objc
+ (instancetype) criticalSoundNamed:(UNNotificationSoundName) name;
```

## Return Value

A sound object representing a custom critical alert sound.

## Discussion

Critical alerts ignore the mute switch and Do Not Disturb. They require a special entitlement issued by Apple.

## Parameters

- `name`: The name of the sound file to play. This file must be located in the current executable’s main bundle or in the `Library/Sounds` directory of the current app container directory. If files exist at both locations, the system uses the file from the `Library/Sounds` directory. This parameter must not be `nil`.

## See Also

### Getting Critical Sounds
- [class var defaultCritical: UNNotificationSound](./defaultcritical.md)
  The default sound used for critical alerts.
- [class func defaultCriticalSound(withAudioVolume: Float) -> Self](./defaultcriticalsound%28withaudiovolume%29.md)
  Creates a sound object that plays the default critical alert sound at the volume you specify.
- [class func criticalSoundNamed(UNNotificationSoundName, withAudioVolume: Float) -> Self](./criticalsoundnamed%28_,withaudiovolume%29.md)
  Creates a custom sound object for critical alerts with the volume you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsound/criticalsoundnamed(_:))*