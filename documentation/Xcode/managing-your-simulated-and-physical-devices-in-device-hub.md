# Managing your simulated and physical devices in Device Hub

**Framework**: Xcode

Add custom simulators and pair physical devices with your Mac so you can choose them as run destinations in Xcode.

#### Overview

Use Device Hub to add specific simulator configurations and pair physical devices that you want to test your app on.

To open Device Hub from Xcode without running your app, choose Manage Devices… from the run destination pop-up menu or choose Xcode > Open Developer Tool > Device Hub. Otherwise, when you run your app on a simulator, Device Hub opens a compact window that you can expand to show the sidebar.

In the Device Hub sidebar, only the simulators that you add here or that you previously chose as run destinations in Xcode appear. Similarly, only the physical devices that you pair with your Mac appear. To view the available simulated or physical devices separately, choose Simulators or Physical Devices from the filter pop-up menu at the top of the sidebar.

![A screenshot of the Device Hub expanded window showing simulated and physical devices in the sidebar with the filter menu displaying, an Apple TV device in the canvas in the middle, and the settings inspector on the right.](/images/com.apple.Xcode/device-hub-manage-devices@2x.png)

To see the status of a device, select it in the sidebar and any issues appear in the canvas on the right. If you’re currently running an app on the device or you started a simulated device, the device screen appears instead. To explore more information about a device in the inspector, click the Info button in the far right of the toolbar.

For information on running your app on devices that you manage in Device Hub, see [`Running your app on simulated or physical devices`](running-your-app-on-simulated-or-physical-devices.md).

#### Add Additional Simulators

You can add simulators for specific platforms and operating system versions that don’t appear in the Xcode run destination pop-up menu.

To add a simulator with a specific configuration, click the Add Device button (+) at the top of the sidebar and choose a device under Simulators from the pop-up menu. In the dialog, optionally enter a name for the simulator, choose the operating system version and model, and click Create. The simulator appears under Available in the sidebar.

![A screenshot of dialog that appears when you choose a simulator from the Add Device pop-up menu.](/images/com.apple.Xcode/add-additional-simulators@2x.png)

To remove a simulator from Device Hub, Control-click it in the sidebar and choose Remove.

#### Pair Physical Devices Wirelessly to Your Mac

> ❗ **Important**: Upgrade your iPhone or iPad to iOS or iPadOS 27 or later to wirelessly pair it; otherwise, use a cable.

First, ensure that the device is on the same Wi-Fi network as your Mac so that it can discover it.

Then click the Add Device button (+) in the toolbar and choose Pair Nearby Device… from the pop-up menu. Then choose the type of device from the buttons at the top of the sheet and follow the instructions that appear. For example, you may need to enable Developer Mode on the device before you can continue.

For devices that you’re pairing for the first time, the Developer Mode setting may not appear on the device until you begin the pairing process in Device Hub. To pair an Apple Watch, enable Developer Mode on both the companion iPhone and the Apple Watch. For more information, see [`Enabling Developer Mode on a device`](enabling-developer-mode-on-a-device.md).

For tvOS and visionOS devices, make sure that your Wi-Fi network has IPv6 enabled. Then broadcast the device to the target Mac over the local network:

- In visionOS, choose Settings > General > Remote Devices.
- In tvOS, choose Settings > Remotes and Devices > Remote App and Devices.

If a dialog appears on your Mac asking you to allow it to find devices, click Allow. In the Device Hub sheet, select the device that it discovers and click Next. In the next sheet, enter the PIN that appears on your device.

![A screenshot of the sheet that appears when you wirelessly pair a physical device with Apple TV selected and the device-specific instructions below.](/images/com.apple.Xcode/wirelessly-pair-device@2x.png)

When the Trust This Computer dialog appears on the device, tap Trust. For an Apple Watch connected to an iPhone, tap Trust on both the iPhone and the Apple Watch. If you accidentally dismiss the trust dialog, or the device doesn’t immediately appear in Device Hub after you tap Trust, try restarting the device.

After completing the steps, the device appears in the Device Hub sidebar. If you upgrade the operating system later, you’ll need to pair the device again. To explicitly unpair a device, Control-click the device in the sidebar and choose Unpair.

#### Pair Devices Using a Cable

Connect the device with an appropriate cable to your Mac. If a Trust This Computer dialog appears on the device, tap Trust.

In Device Hub, select the device in the sidebar and follow the instructions in the canvas. If a Pair button appears, click it. If necessary, enable Developer Mode on the device. For more information, see [`Enabling Developer Mode on a device`](enabling-developer-mode-on-a-device.md).

For Apple Watch, pair the companion iPhone first. For Apple Watch Series 5 or older, make sure that your Mac is connected to the same Bonjour-compatible Wi-Fi network as your watch. Otherwise, your Apple Watch doesn’t appear.

After completing the steps, the device appears under Available in the Device Hub sidebar and a View Screen button appears in the canvas. You can disconnect the physical cable and run apps on the device through Xcode using Wi-Fi with IPv6 enabled on the same network as your Mac.

> **Note**: For earlier versions of iOS, Xcode requires your iPhone to remain physically connected to your Mac to run your app on any model of Apple Watch.

## See Also

- [Running your app on simulated or physical devices](running-your-app-on-simulated-or-physical-devices.md)
  Launch your app on a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a physical device paired with your Mac.
- [Enabling Developer Mode on a device](enabling-developer-mode-on-a-device.md)
  Grant or deny permission for locally installed apps to run in iOS, iPadOS, watchOS, and visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/managing-your-simulated-and-physical-devices-in-device-hub)*