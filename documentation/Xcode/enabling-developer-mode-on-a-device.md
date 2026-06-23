# Enabling Developer Mode on a device

**Framework**: Xcode

Grant or deny permission for locally installed apps to run in iOS, iPadOS, watchOS, and visionOS.

#### Overview

Enable Developer Mode on a device to run your app on the device through Xcode. Developer Mode protects people from inadvertently installing potentially harmful software, and reduces attack vectors exposed by developer-only functionality.

The feature doesn’t affect ordinary installation techniques, such as buying apps from the App Store or participating in a TestFlight team. Instead, Developer Mode focuses on scenarios like building and running an app from Xcode, or installing an `.ipa` file with [`Apple Configurator`](https://developer.apple.comhttps://support.apple.com/apple-configurator). In these cases, the device explicitly asks the person using it to confirm that they’re a developer, and aware of the risks of installing development-signed software.

When you start pairing a device, Device Hub displays a message when you need to turn on Developer Mode or when Developer Mode is turned off on a previously paired device. For more information, see [`Managing your simulated and physical devices in Device Hub`](managing-your-simulated-and-physical-devices-in-device-hub.md).

After you turn on Developer Mode, Developer settings appear on the device that help you test and debug your app.

> **Note**: Developer Mode only appears in Settings if you initiate pairing or if you previously paired the device to a Mac. In tvOS, there’s no Developer Mode. Just pair your Apple TV using Device Hub and Developer Settings appear on the device.

##### Turn on Developer Mode in Ios Ipados Watchos and Visionos

In the Privacy & Security settings on the device, turn on the Developer Mode switch under Security. An alert appears to warn you that Developer Mode reduces the security of your device. To continue turning on Developer Mode, tap the Restart button in the alert.

After the device restarts, another alert appears confirming that you want to turn on Developer Mode. In iOS and iPadOS, swipe up, tap Enable in the dialog, and enter your device passcode.

In watchOS, tap Turn On. Tap Trust in the next dialog, if it appears, and enter your device passcode to confirm.

##### Turn Off Developer Mode

To turn off Developer Mode, turn off the Developer Mode switch in Settings > Privacy & Security and restart the device. After you turn off Developer Mode, you can’t run apps from Xcode on the device until you turn on Developer Mode again.

## See Also

- [Running your app on simulated or physical devices](running-your-app-on-simulated-or-physical-devices.md)
  Launch your app on a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a physical device paired with your Mac.
- [Managing your simulated and physical devices in Device Hub](managing-your-simulated-and-physical-devices-in-device-hub.md)
  Add custom simulators and pair physical devices with your Mac so you can choose them as run destinations in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device)*