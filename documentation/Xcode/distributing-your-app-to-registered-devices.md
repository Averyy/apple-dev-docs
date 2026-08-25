# Distributing your app to registered devices

**Framework**: Xcode

Test your app on devices that you register in your developer account.

#### Overview

Before collecting feedback from beta testers using TestFlight, you can distribute builds to a limited set of testers on known devices without having to go through beta app review.

First, use either Xcode or your [`developer account`](https://developer.apple.comhttps://developer.apple.com/programs/) to register the devices that you want to test with. Consider that your team has a limited number of devices per product family per year for both development and testing. Then archive and export your app for distribution.

Alternatively, distribute your app to testers using TestFlight. For more information, see [`Distributing your app for beta testing and releases`](distributing-your-app-for-beta-testing-and-releases.md).

#### Register Devices Automatically in Xcode

Xcode can manage the certificates, identifiers, and profiles for you.

First, use Device Hub to pair the physical devices with your Mac, either wirelessly or with a cable. For more information, see [`Managing your simulated and physical devices in Device Hub`](managing-your-simulated-and-physical-devices-in-device-hub.md).

In the Signing & Capabilities pane under Signing, toggle “Automatically manage signing” on. For each device, choose it as the run destination, click the Register Device button under Signing or in the popover if it appears, and click Run. Xcode registers and adds the device to the provisioning profile.

For more information on running apps through Xcode, see [`Running your app on simulated or physical devices`](running-your-app-on-simulated-or-physical-devices.md).

#### Register Devices in Your Developer Account

First, collect the unique device identifiers for your iPhone, iPad, Apple TV, Apple Vision Pro, or Apple Watch devices using either Device Hub or Finder. To get the device identifiers for Mac computers, use System Information. For more information, see [`Locating device identifiers`](locating-device-identifiers.md).

Then upload a file containing the device names and identifiers to your developer account. For more information, see [`Register multiple devices`](https://developer.apple.comhttps://developer.apple.com/help/account/register-devices/register-multiple-devices) in Developer Account Help.

For more information on managing your devices, including disabling devices you no longer use, see [`Devices overview`](https://developer.apple.comhttps://developer.apple.com/help/account/devices/devices-overview) in Developer Account Help.

#### Create an App Archive

In the project window, choose a target and a run destination from the Scheme toolbar menu. Choose Product > Archive to build the target. Xcode then displays the archive in the Archives organizer. If you select a simulator for your run destination, Xcode builds an archive matching the build-only device type for that simulator.

> **Note**: For an app built with Mac Catalyst, create separate archives for the iPad and Mac Catalyst builds. When creating the archive for the Mac Catalyst build, choose the run destination that includes Mac Catalyst in its name. For an app built with Designed for iPad, create a single archive using iPad as the run destination or any run destination that includes Designed for iPad in its name. These run destinations produce the same archive.

#### Export the App Archive

In the Archives organizer, export a version of the app to distribute to testers:

1. Select the archive and click Distribute App.
2. Select Debugging and click Distribute.
3. Review the build details in the next sheet and click Export.
4. Select a location to save the exported app and click Export.

Xcode creates a folder that contains a few files. For iOS, iPadOS, tvOS, visionOS, or watchOS apps, the folder contains the iOS Package Archive file (with an `.ipa` extension). For macOS apps, it contains the app bundle.

#### Install the App on Registered Devices

Next, give the exported files to testers so they can install the app on their registered devices using Device Hub or Apple Configurator. For more information, see [`Install apps on devices`](managing-apps-on-devices#Install-apps-on-devices.md). For macOS apps, drag the app bundle to the `/Applications` folder or another folder of your choice on the Mac.

> ❗ **Important**: To run your iOS, iPadOS, visionOS, or watchOS app that you install from an iOS Package Archive, enable Developer Mode on that device. For more information, see [`Enabling Developer Mode on a device`](enabling-developer-mode-on-a-device.md).

#### Test Your App on Specific Devices

For iOS, iPadOS, tvOS, visionOS, and watchOS apps, you can have finer control over the test devices using an ad hoc provisioning profile for distribution that you create in your developer account.

To create a provisioning profile containing a subset of devices, see [`Create an ad hoc provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/provisioning-profiles/create-an-ad-hoc-provisioning-profile) in Developer Account Help, where you select which registered devices to include.

To update an existing provisioning profile after you add or remove devices, see [`Edit, download, or delete provisioning profiles`](https://developer.apple.comhttps://developer.apple.com/help/account/provisioning-profiles/edit-download-or-delete-profiles).

Then choose your custom provisioning profile when you export your archive for distribution. Testers can run your app only on the devices that you add to the provisioning profile.

## See Also

- [Notarizing macOS software before distribution](../security/notarizing-macos-software-before-distribution.md)
  Give users even more confidence in your macOS software by submitting it to Apple for notarization.
- [Distributing your app for beta testing and releases](distributing-your-app-for-beta-testing-and-releases.md)
  Release your app to beta testers and users.
- [Locating device identifiers](locating-device-identifiers.md)
  Get the unique identifier for a device before registering it in your developer account.
- [Packaging Mac software for distribution](packaging-mac-software-for-distribution.md)
  Build a zip archive, disk image, or installer package for distributing your Mac software.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices)*