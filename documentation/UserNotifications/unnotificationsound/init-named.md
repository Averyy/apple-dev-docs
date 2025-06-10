# init(named:)

**Framework**: User Notifications  
**Kind**: init

Creates a sound object that represents a custom sound file.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
convenience init(named name: UNNotificationSoundName)
```

#### Return Value

A sound object representing the custom sound.

#### Discussion

This method searches for sound files in the following locations, in order:

1. The `/Library/Sounds` directory, where  is the app’s container directory.
2. The `/Library/Sounds` directory, where  is one of the app’s shared group container directories. For information about how to configure group containers for your app, see [`Configure app groups`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev8dd3880fe).
3. The main bundle of the current executable.

The method chooses the first file it finds with the specified name.

## Parameters

- `name`: The name of the sound file to play. This parameter must not be  .

## See Also

- [class var `default`: UNNotificationSound](unnotificationsound/default.md)
  Returns an object representing the default sound for notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsound/init(named:))*