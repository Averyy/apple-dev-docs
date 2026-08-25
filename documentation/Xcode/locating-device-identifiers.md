# Locating device identifiers

**Framework**: Xcode

Get the unique identifier for a device before registering it in your developer account.

#### Overview

To register one or more devices using your developer account, you first collect the device identifiers. Typically, you register multiple devices using your developer account to test your app internally before uploading builds to App Store Connect. Later, you can use TestFlight to distribute beta builds to testers without needing to register their devices.

For more information on distributing your app to a limited set of people on known devices, see [`Distributing your app to registered devices`](distributing-your-app-to-registered-devices.md).

#### Locate Device Identifiers Using Device Hub

For iOS, iPadOS, tvOS, visionOS, and watchOS devices, you can use Device Hub to get identifiers. If the physical device doesn’t appear in Device Hub, pair it with your Mac as described in [`Managing your simulated and physical devices in Device Hub`](managing-your-simulated-and-physical-devices-in-device-hub.md).

1. Select the device in the sidebar.
2. In the inspector, click Info in the toolbar.
3. Under Hardware Properties, copy the device ID that appears in the UDID field.

![A screenshot of Device Hub showing a physical device selected in the sidebar on the left, an iPhone device mirrored in the canvas in the middle, and the device ID shown in the Info inspector on the right.](/images/com.apple.Xcode/locating-device-id-device-hub@2x.png)

If the UDID field doesn’t appear, click Edit Visibility at the bottom of the inspector. Toggle on the UDID property and others that you want to show and toggle off properties you want to hide. Click Done.

#### Locate Device Identifiers Using Finder

For iOS, iPadOS, tvOS, visionOS, and watchOS devices, you can use Finder to get identifiers without pairing the devices with your Mac using Device Hub.

1. Connect your device to your Mac.
2. In Finder, select the device under Locations.
3. If a Trust button appears, click it, and on the device, click Trust in the dialog that appears and enter your passcode.
4. In the toolbar under the device name, click the device family twice to show the device ID (UDID). Finder rotates through other device information with each click.
5. Control-click the device ID and choose Copy UDID from the contextual menu.

If the Locations section doesn’t appear in Finder, see [`Customize the Finder toolbar and sidebar on Mac`](https://developer.apple.comhttps://support.apple.com/guide/mac-help/customize-finder-toolbar-sidebar-mac-mchlp3011/mac).

#### Locate Mac Device Identifiers Using System Information

Use System Information if you want to register a Mac that you don’t use for development.

1. In System Settings > General > About, scroll to the bottom and click System Report.
2. Select Hardware in the sidebar.
3. Copy the device ID that appears in the Provisioning UDID field.

![A screenshot of System Information showing Hardware selected in the sidebar on the left and the device ID displayed in the detail area on the right.](/images/com.apple.Xcode/locating-macos-device-id@2x.png)

## See Also

- [Managing apps on devices](managing-apps-on-devices.md)
  Find, add, and remove apps installed for testing on simulated and physical devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/locating-device-identifiers)*