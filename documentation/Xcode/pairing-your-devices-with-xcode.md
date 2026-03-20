# Pairing your devices with Xcode

**Framework**: Xcode

Include devices in the list of run destinations for your app in Xcode.

#### Overview

You pair a device with Xcode to include it in the list of run destinations for when you build and run your app using Xcode. First check the status of your devices in the Devices pane in the Devices and Simulators window. Then connect your device with a cable or over Wi-Fi to your Mac so Xcode discovers it. Then initiate the pairing process and follow the steps that appear in the Devices and Simulators window.

![A screenshot of the Devices and Simulators window showing the Devices tab selected with connected, disconnected, and discovered devices in the sidebar and the details of a connected device on the right.](https://docs-assets.developer.apple.com/published/565db48705747b75d4898e4ef4a93562/devices-window-connection-status%402x.png)

For more information on running your app on real devices, see [`Running your app in Simulator or on a device`](running-your-app-in-simulator-or-on-a-device.md).

##### Manage Your Real Devices in Xcode

To manage connections to your real devices, choose Window > Devices and Simulators and select the Devices tab in the sidebar. Xcode shows the currently connected and disconnected devices, as well as new devices that Xcode detects. Unpaired devices appear under Discovered and previously paired devices appear under Connected or Disconnected. Select a device in the sidebar to see its status as a run destination in the detail area. Read the alert in the yellow box to help you fix issues and guide you through the pairing process.

##### Discover New Devices

Before you can pair a device, Xcode needs to discover the device. That is, the device needs to appear under Discovered on the Devices pane in the Devices and Simulators window.

To begin pairing iOS or iPadOS devices, connect the device with an appropriate cable to your Mac. For watchOS, pair the companion iOS device first and then follow additional watchOS instructions below. For tvOS, you can use a cable or Wi-Fi to connect to your Mac.

To discover tvOS and visionOS devices using Wi-Fi, ensure that the device is on the same Wi-Fi network as your Mac. Then broadcast the device to the target Mac over the local network. In visionOS, choose Settings > General > Remote Devices. In tvOS, choose Settings > Remotes and Devices > Remote App and Devices. If a dialog appears on your Mac asking you to allow Xcode to find devices, click Allow.

##### Pair Real Devices

On the Devices pane in the Devices and Simulators window, select the device you want to pair under Discovered, and follow the instructions that appear in the detail area or yellow box in the detail area. Xcode automatically starts pairing a device with a physical connection to your Mac.

For tvOS and visionOS devices connected using Wi-Fi with IPv6 enabled, click Pair in the detail area. Then enter the PIN that appears on your device and click Connect. On the device, your Mac appears in Remote App and Devices settings under Devices. In Xcode, select the device in the sidebar of the Devices and Simulators window.

As part of the pairing process, click Trust in the Trust This Computer dialog that appears on the device. If you accidentally dismiss the trust dialog, try reconnecting the cable or restarting the device. After you trust your Mac, Xcode shows the device under Connected on the Devices pane in the Devices and Simulators window.

If a warning appears in a yellow box in the detail area that you need to enable Developer Mode on the device, see [`Enabling Developer Mode on a device`](enabling-developer-mode-on-a-device.md). For devices that you pair for the first time, the Developer Mode setting doesn’t appear on the device until you begin the pairing process.

Before a device is available as a run destination, you may need to wait until Xcode finishes copying shared cache symbols or fixing other compatibility issues. For example, the operating system version on the device needs to be the same or newer than the minimum deployment version in your Xcode project target settings. For more information, see [`Connect real devices to your Mac`](running-your-app-in-simulator-or-on-a-device#Connect-real-devices-to-your-Mac.md).

![A screenshot of the Devices pane of the Devices and Simulators window showing a connected device selected in the sidebar and a message that Xcode is copying shared cache symbols in the detail area on the right.](https://docs-assets.developer.apple.com/published/4410c841cc4e481a192fb3e06e49f7d5/devices-window-copying-cache%402x.png)

When a device appears under Connected in the sidebar without any issues, you can disconnect the physical cable and run apps on the device through Xcode using Wi-Fi with IPv6 enabled on the same network as your Mac.

To unpair a device, Control-click the device under Connected and choose Unpair Device.

##### Pair an Apple Watch with Xcode

After you pair an iPhone with Xcode, any Apple Watch that’s paired with that iPhone appears under Paired Watches in the detail area for the iPhone in the Devices and Simulators window.

To make the Apple Watch available as a run destination, follow instructions on the device to trust the Mac. Also, enable Developer Mode on the Apple Watch, not just the iPhone, as described in [`Enabling Developer Mode on a device`](enabling-developer-mode-on-a-device.md).

If an Apple Watch paired with a connected iPhone doesn’t appear, or appears as unavailable as a run destination in the project window, fix the issue that appears in the yellow box in the detail area in the Devices and Simulators window.

> **Note**: If your Apple Watch is Series 5 or older, make sure that your Mac is connected to the same Bonjour-compatible Wi-Fi network as your watch. Otherwise, your Apple Watch doesn’t appear. For older versions of iOS, Xcode requires your iPhone to remain physically connected to your Mac to run your app on any model of Apple Watch.

## See Also

- [Running your app in Simulator or on a device](running-your-app-in-simulator-or-on-a-device.md)
  Launch your app in a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a device connected to a Mac.
- [Enabling Developer Mode on a device](enabling-developer-mode-on-a-device.md)
  Grant or deny permission for locally installed apps to run in iOS, iPadOS, watchOS, and visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/pairing-your-devices-with-xcode)*