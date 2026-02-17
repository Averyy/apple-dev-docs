# Enabling Developer Mode on a device

**Framework**: Xcode

Grant or deny permission for locally installed apps to run in iOS, iPadOS, watchOS, and visionOS.

#### Overview

You enable Developer Mode on a device to run your app on the device through Xcode. Developer Mode protects people from inadvertently installing potentially harmful software on their devices, and reduces attack vectors exposed by developer-only functionality. The feature doesn’t affect ordinary installation techniques, like buying apps from the App Store or participating in a TestFlight team. Instead, Developer Mode focuses on scenarios like building and running an app from Xcode, or installing an `.ipa` file with [`Apple Configurator`](https://developer.apple.comhttps://support.apple.com/apple-configurator). In these cases, the device explicitly asks the person using it to confirm that they’re a developer, aware of the risks of installing development-signed software.

Before you can turn on Developer Mode, pair your device with Xcode, as described in [`Pairing your devices with Xcode`](pairing-your-devices-with-xcode.md). Xcode displays a message when you need to turn on Developer Mode during the pairing process or when Developer Mode is turned off on a previously connected device.

![A screenshot of the Devices and Simulators window showing the Devices tab selected with a connected device selected in the sidebar and a Developer Mode is turned off warning in the detail area.](https://docs-assets.developer.apple.com/published/ff1baf3a27256a3540ac425ab472bbca/developer-mode-disable-warning%402x.png)

After you pair your device and turn on Developer Mode, you can choose the device as a run destination in the project editor. Also, Developer settings appear on the device that help you test and debug your app. For more information on running your app on a device, see [`Running your app in Simulator or on a device`](running-your-app-in-simulator-or-on-a-device.md).

> **Note**: Developer Mode only appears in Settings if you initiate pairing or if you previously connected the device to Xcode. In tvOS, there’s no Developer Mode. Just pair your Apple TV with Xcode and Developer Settings appear on the device.

##### Turn on Developer Mode in Ios Ipados Watchos and Visionos

In the Privacy & Security settings on the device, toggle the Developer Mode switch under Security to on. An alert appears to warn you that Developer Mode reduces the security of your device. To continue turning on Developer Mode, tap the Restart button in the alert.

After the device restarts, another alert appears confirming that you want to turn on Developer Mode. In iOS and iPadOS, swipe up and tap Enable in the dialog. In watchOS, tap Turn On. Tap Trust in the next dialog, if it appears, and enter your device passcode to confirm.

##### Turn Off Developer Mode

To turn off Developer Mode, toggle the Settings > Privacy & Security > Developer Mode switch off and restart the device. After you turn off Developer Mode, you can’t run apps from Xcode on the device until you turn on Developer Mode again.

## See Also

- [Running your app in Simulator or on a device](running-your-app-in-simulator-or-on-a-device.md)
  Launch your app in a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a device connected to a Mac.
- [Pairing your devices with Xcode](pairing-your-devices-with-xcode.md)
  Include devices in the list of run destinations for your app in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device)*