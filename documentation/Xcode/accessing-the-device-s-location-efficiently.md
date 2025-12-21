# Accessing the device’s location efficiently

**Framework**: Xcode

Use Core Location features to manage energy use, receive updates, and minimize location update frequency.

#### Overview

Discovering a person’s location — particularly to a high [`desiredAccuracy`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/desiredAccuracy) — requires combining information from multiple device subsystems that each consume power while they’re active. Minimize the frequency with which your app requests location updates, and don’t leave location updates running when your app doesn’t need them.

Use [`CLLocationUpdate`](https://developer.apple.com/documentation/CoreLocation/CLLocationUpdate) to receive updates from the system when the device’s location changes. If the device becomes stationary, Core Location sets the [`stationary`](https://developer.apple.com/documentation/CoreLocation/CLLocationUpdate/stationary) flag and stops providing updates until the device moves again. When this happens, if you don’t expect movement again soon, consider stopping location updates and using [`CLMonitor`](https://developer.apple.com/documentation/CoreLocation/CLMonitor-2r51v) to get notified of significant changes to the device’s location. Set [`distanceFilter`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/distanceFilter) to the distance the device needs to move before the system notifies your app.

If you need to receive location updates when your app is in the background, use [`CLBackgroundActivitySession`](https://developer.apple.com/documentation/CoreLocation/CLBackgroundActivitySession-3mzv3), or call [`requestAlwaysAuthorization()`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/requestAlwaysAuthorization()). For more information, see [`Handling location updates in the background`](https://developer.apple.com/documentation/CoreLocation/handling-location-updates-in-the-background). However, only register for background location updates if your app’s functionality doesn’t work without it, as background updates increase your app’s energy use.

## See Also

- [Reducing networking and Bluetooth power usage](reducing-networking-and-bluetooth-power-usage.md)
  Schedule requests strategically and minimize background network activity to decrease your app’s energy use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/accessing-the-device-s-location-efficiently)*