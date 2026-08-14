# Enabling Background Sessions

**Framework**: WatchKit

Enable the background mode for audio, location updates, remote notifications, or workouts.

#### Overview

To receive background notifications or run background sessions, your app needs to enable the corresponding background mode. Add the Background Modes capability to your WatchKit extension, and then select the desired modes. Each mode sets its respective keys in the extension’s `Info.plist` file.

![A screenshot showing the background modes.](/images/com.apple.watchkit/media-3694647@2x.png)

The Remote notification mode lets your app receive remote, background notifications. When a background notification arrives, the system wakes or launches your app to the background and gives it 30 seconds to update the app. For more information, see [`Pushing background updates to your App`](https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app).

The Audio, Location updates, and Workout processing modes let your app run the respective background sessions. Your app must start the session in the foreground, but the session continues to run when your app transitions to the background. Also, while the session is running, Apple Watch displays your app whenever the user raises their wrist. If the user presses the digital crown to navigate back to the watch face, the system displays an icon above the status bar, indicating that the session is still active.

- Use an [`HKWorkoutSession`](https://developer.apple.com/documentation/healthkit/hkworkoutsession) object to start and stop workouts. For more information, see [`Running workout sessions`](https://developer.apple.com/documentation/healthkit/running-workout-sessions).
- Use the [`AVAudioSession`](https://developer.apple.com/documentation/avfaudio/avaudiosession) class to play extended audio files in the background. For more information see [`Playing Background Audio`](playing-background-audio.md).
- Use a [`CLLocationManager`](https://developer.apple.com/documentation/corelocation/cllocationmanager) object to start a continuous background location session. For more information, see [`allowsBackgroundLocationUpdates`](https://developer.apple.com/documentation/corelocation/cllocationmanager/allowsbackgroundlocationupdates).

## See Also

- [Playing Background Audio](playing-background-audio.md)
  Enable background audio in your app to provide a seamless playback experience.
- [WKBackgroundModes](../bundleresources/information-property-list/wkbackgroundmodes.md)
  The services a watchOS app provides that require it to continue running in the background.
- [UIBackgroundModes](../bundleresources/information-property-list/uibackgroundmodes.md)
  Services provided by an app that require it to run in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/enabling-background-sessions)*