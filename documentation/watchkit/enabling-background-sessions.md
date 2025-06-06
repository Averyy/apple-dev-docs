# Enabling Background Sessions

**Framework**: Watchkit

Enable the background mode for audio, location updates, remote notifications, or workouts.

#### Overview

To receive background notifications or run background sessions, your app needs to enable the corresponding background mode. Add the Background Modes capability to your WatchKit extension, and then select the desired modes. Each mode sets its respective keys in the extension’s `Info.plist` file.

![A screenshot showing the background modes.](https://docs-assets.developer.apple.com/published/1a4e02853adfbec31f913f6036f856d1/media-3694647%402x.png)

The Remote notification mode lets your app receive remote, background notifications. When a background notification arrives, the system wakes or launches your app to the background and gives it 30 seconds to update the app. For more information, see [`Pushing background updates to your App`](https://developer.apple.com/documentation/UserNotifications/pushing-background-updates-to-your-app).

The Audio, Location updates, and Workout processing modes let your app run the respective background sessions. Your app must start the session in the foreground, but the session continues to run when your app transitions to the background. Also, while the session is running, Apple Watch displays your app whenever the user raises their wrist. If the user presses the digital crown to navigate back to the watch face, the system displays an icon above the status bar, indicating that the session is still active.

- Use an [`HKWorkoutSession`](https://developer.apple.com/documentation/HealthKit/HKWorkoutSession) object to start and stop workouts. For more information, see [`Running workout sessions`](https://developer.apple.com/documentation/HealthKit/running-workout-sessions).
- Use the [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) class to play extended audio files in the background. For more information see [`Playing Background Audio`](playing-background-audio.md).
- Use a [`CLLocationManager`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager) object to start a continuous background location session. For more information, see [`allowsBackgroundLocationUpdates`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/allowsBackgroundLocationUpdates).

## See Also

- [Playing Background Audio](playing-background-audio.md)
  Enable background audio in your app to provide a seamless playback experience.
- [WKBackgroundModes](../BundleResources/Information-Property-List/WKBackgroundModes.md)
  The services a watchOS app provides that require it to continue running in the background.
- [UIBackgroundModes](../BundleResources/Information-Property-List/UIBackgroundModes.md)
  Services provided by an app that require it to run in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/enabling-background-sessions)*