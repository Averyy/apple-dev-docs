# Responding to power notifications

**Framework**: Xcode

Adopt more power-efficient strategies to prolong the device’s battery life.

#### Overview

Certain situations cause a device to reduce the amount of work it does and the amount of power it uses. People who want to increase the time before their device needs charging can turn on Low Power Mode. When a device is in Low Power Mode, the system enacts energy-saving measures, including reducing animations, and increasing the time between certain power-consuming actions like fetching data over the network.

Additionally, if the system detects that the temperature is too high, it reduces the amount of power it uses until the temperature decreases.

Register for system notifications about power- and thermal-state changes so you can take steps to help the system conserve energy and reduce its temperature.

##### Detect and React to Power State Notifications

In your app, register for [`NSProcessInfoPowerStateDidChange`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSProcessInfoPowerStateDidChange) to discover when the device’s power state changes. When you receive the notification, query the value of [`isLowPowerModeEnabled`](https://developer.apple.com/documentation/Foundation/ProcessInfo/isLowPowerModeEnabled) to determine if the system’s in Low Power Mode.

If Low Power Mode is active, take additional steps to help the system conserve energy, including:

- Pausing any optional activities
- Reducing display updates
- Minimizing animations
- Reducing the frequency of network connections
- Stopping location updates

##### Detect and React to Thermal State Notifications

In your app, register for [`thermalStateDidChangeNotification`](https://developer.apple.com/documentation/Foundation/ProcessInfo/thermalStateDidChangeNotification) to discover when the device’s thermal state changes. When you receive the notification, adjust your app’s behavior according to the value of [`thermalState`](https://developer.apple.com/documentation/Foundation/ProcessInfo/thermalState-swift.property):

## See Also

- [Scheduling CPU work efficiently](scheduling-cpu-work-efficiently.md)
  Use concurrent programming and adjust the prioritization of background activities to improve the performance of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/responding-to-power-notifications)*