# Enabling Developer Mode on a device

**Framework**: Xcode

Grant or deny permission for locally installed apps to run on iOS, iPadOS, visionOS, and watchOS devices.

#### Overview

Developer Mode protects people from inadvertently installing potentially harmful software on their devices, and reduces attack vectors exposed by developer-only functionality. The feature doesn’t affect ordinary installation techniques, like buying apps from the App Store or participating in a TestFlight team. Instead, Developer Mode focuses on scenarios like performing a Build and Run in Xcode, or installing an `.ipa` file with [`Apple Configurator`](https://developer.apple.comhttps://support.apple.com/apple-configurator). In these cases, the device explicitly asks the person using it to confirm that they’re a developer, aware of the risks of installing development-signed software.

##### Enable Developer Mode

To build and run your app on an iOS, visionOS, or watchOS device, you need to pair your device with Xcode and enable Developer Mode on the device. Xcode displays a message when you need to enable Developer Mode if you choose the device as the run destination, click the Run button, or select the device in the Devices and Simulators window.

To enable Developer Mode, first choose the device as the run destination and click the Run button. If a dialog appears stating that the device must opt into Developer Mode, click Cancel. Then open the Privacy & Security settings on the device and tap the Developer Mode option that appears under Security. On a watchOS device, go to Settings > Privacy & Security > Developer Mode. The Developer Mode option appears after the first time you try to run your app from Xcode on the device.

![A screenshot of the iOS Settings app showing a switch labeled Developer Mode. Under this, a description reads: If you’re developing apps for Apple products, Developer Mode allows you to use features that are required for app development. When Developer Mode is turned on, your device security will be reduced.](https://docs-assets.developer.apple.com/published/4491abbd02b1b94ab600c087177fcf6d/enabling-developer-mode-on-a-device-03%402x.png)

Toggle the Developer Mode switch to the on position. Settings displays an alert to warn you that Developer Mode reduces the security of your device. To continue enabling Developer Mode, tap the Restart button in the alert.

After the device restarts and you unlock it, the device shows an alert confirming that you want to enable Developer Mode. To acknowledge the reduction in security protection in exchange for allowing Xcode and other tools to execute code, tap Enable, and when the next prompt appears, enter your device passcode.

Now you can install and run apps from Xcode on the device. After the first time you enable Developer Mode, Xcode doesn’t ask you to enable it again unless you disable Developer Mode or restore the device.

##### Disable Developer Mode

To disable Developer Mode on the device, go to Settings > Privacy & Security > Developer Mode and tap Developer Mode. Toggle the Developer Mode switch to the off position. After you disable Developer Mode, you can’t run apps from Xcode on the device until you enable Developer Mode again.

## See Also

- [Running your app in Simulator or on a device](running-your-app-in-simulator-or-on-a-device.md)
  Launch your app in a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a device connected to a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device)*