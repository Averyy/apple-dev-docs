# Reducing your app’s battery use

**Framework**: Xcode

Adopt design principles and recommended APIs to consume less power.

#### Overview

When your app performs intensive computation, or uses device features like location and networking, it causes the device to use more energy. Significant energy use can result in degraded performance both for your app, and the overall experience of using the device. For more information, see [`Analyzing your app’s battery use`](analyzing-your-app-s-battery-use.md).

Use the following three-stage process to reduce your app’s energy use:

1. Do less work.
2. Work more efficiently.
3. Avoid misusing APIs.

The following sections describe approaches to take at each stage.

##### Reduce Overall Computation

Consider whether your app can update its state less frequently. Look for opportunities to remove activity altogether, so that your app avoids consuming energy using device subsystems that it doesn’t need to use.

If your app performs energy-intensive operations continuously, such as requesting the device’s location, change your app to only do this when someone requests it. Limiting your app’s use of location services to times when someone explicitly requests it also makes it easier for someone to understand the privacy implications of your app, because they can understand the relationship between their intent and how your app uses their data. For more information, see [`Foundations > Privacy`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/privacy) in the Human Interface Guidelines.

##### Improve the Power Efficiency of Tasks in Your App

Prefer high-level frameworks that are optimized to make efficient use of hardware, over direct low-level access to hardware that might be harder to use efficiently. Follow guidance in the documentation for specific frameworks to use them efficiently.

##### Use Apis Efficiently

Follow best-practice recommendations to use APIs in energy-efficient ways. The following articles present guidance for reducing energy use related to specific technologies.

## Topics

### Essentials
- [Scheduling CPU work efficiently](scheduling-cpu-work-efficiently.md)
  Use concurrent programming and adjust the prioritization of background activities to improve the performance of your app.
- [Responding to power notifications](responding-to-power-notifications.md)
  Adopt more power-efficient strategies to prolong the device’s battery life.
### Graphics and sound
- [Improving your app’s rendering efficiency](improving-your-app-s-rendering-efficiency.md)
  Optimize view updates by minimizing unnecessary redraws and using efficient update strategies.
- [Reducing power usage when capturing media](reducing-power-usage-when-capturing-media.md)
  Optimize device camera power usage by stopping sessions when not needed and choosing appropriate video formats.
### Networking and location
- [Reducing networking and Bluetooth power usage](reducing-networking-and-bluetooth-power-usage.md)
  Schedule requests strategically and minimize background network activity to decrease your app’s energy use.
- [Accessing the device’s location efficiently](accessing-the-device-s-location-efficiently.md)
  Use Core Location features to manage energy use, receive updates, and minimize location update frequency.
### Storage
- [Reducing disk writes](reducing-disk-writes.md)
  Improve your app’s responsiveness by optimizing how it writes data to permanent storage.

## See Also

- [Analyzing your app’s battery use](analyzing-your-app-s-battery-use.md)
  Increase the available use time for your app on a single battery charge by reducing your appʼs power consumption.
- [Measuring your app’s power use with Power Profiler](measuring-your-app-s-power-use-with-power-profiler.md)
  Profile your app’s power impact whether or not your device is connected to Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-your-app-s-battery-use)*