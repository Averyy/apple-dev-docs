# Distributing your app to registered devices

**Framework**: Xcode

Register devices in your developer account and deploy your app to them for testing.

#### Overview

Before [`Distributing your app for beta testing and releases`](distributing-your-app-for-beta-testing-and-releases.md), you can distribute progress builds to a limited set of users on known devices, without having to go through beta app review. To distribute to this group of users, register their devices in your [`developer account`](https://developer.apple.comhttps://developer.apple.com/programs/). You can register a limited number of devices, per product family per year, that your team uses for development and testing.

##### Prepare for Your Build

To prepare to distribute your build, you need:

- An App ID that you set up for your app in your [`developer account`](https://developer.apple.comhttps://developer.apple.com/programs/).
- A signing certificate with the public and private key. On iOS, iPadOS, tvOS, visionOS, and watchOS you need a distribution certificate; on macOS you need a development certificate. For more information on signing certificates, see [`Certificates`](https://developer.apple.comhttps://developer.apple.com/support/certificates/).
- A list of test devices registered in your developer account.
- A provisioning profile for your app and list of test devices. On iOS, iPadOS, tvOS, visionOS, and watchOS you need a distribution profile; on macOS you need a development profile.

If you choose the default automatic signing, Xcode creates the provisioning profiles for you, that include all your registered devices; for more advanced cases like large teams with restricted access to signing assets or to only include a subset of your registered devices, prepare your provisioning assets manually. In both automatic and manual provisioning, you need to gather and add your list of test devices to your developer account. When you manually provision a profile, update your provisioning profile after adding test devices.

Each iOS, iPadOS, macOS, tvOS, visionOS, and watchOS device has a persistent, unique identifier referred to as a device ID. When you use automatic signing, Xcode registers the device for you. Otherwise, you need to collect the device ID and register the device in your developer account.

##### Register Devices Automatically in Xcode

When you use automatic signing, Xcode registers the connected device or Mac for you. For iOS, iPadOS, or tvOS attach your device to your computer, and select Trust if the device asks to trust your computer. For watchOS, attach the paired phone for your watchOS device to your computer.

In Xcode, select your attached device as the run destination, and build and run your app. For more information on simulated apps, see [`Running your app in Simulator or on a device`](running-your-app-in-simulator-or-on-a-device.md). If your device needs to be registered, click the Register button in the dialog that Xcode displays, and Xcode registers and adds the device to your provisioning profile.

##### Collect Device Identifiers Ios Ipados Tvos Visionos Watchos

When you use manual signing, start by collecting the device identifier for your iOS, iPadOS, tvOS, visionOS, or watchOS device by using either Finder or Xcode.

Attach your device to your Mac with a cable, and select Trust if your device asks to trust your computer. For watchOS, attach the phone, to which your watch is paired, with to your Mac and use Xcode to find the identifier.

Using the Finder:

1. Locate your device under the Locations section in the sidebar. For more information on what to do if the Locations section is not visible, see [`Customize the Finder toolbar and sidebar on Mac`](https://developer.apple.comhttps://support.apple.com/guide/mac-help/customize-finder-toolbar-sidebar-mac-mchlp3011/mac).
2. Select your device, then click the label below the device name in the info pane once to see the device’s serial number, UDID, and model. Additional clicks rotate through other device information, such as model and storage space, and IMEI and MEID.
3. Control-click the label to copy the device ID, which the UI labels as UDID.

Using Xcode:

1. Select Windows > Devices and Simulators, then select the Devices tab.
2. Select your device under the Connected list.
3. Highlight the device ID, which the UI labels as Identifier, to copy it.

##### Collect Device Identifiers Macos

To find the device ID for your Mac:

1. Choose Apple menu > About this Mac.
2. Click System Report.
3. Select Hardware to see the Hardware Overview; the UI displays the device ID as Hardware UUID (in macOS 10.15 and earlier) or Provisioning UDID (in macOS 11.0 and later).
4. Highlight the Hardware UUID or Provisioning UDID to copy it.

##### Register Devices in Your Developer Account

After you collect the device IDs, you can register them all at once by putting the device names and identifiers in a file. Sign into your developer account, then:

1. Select Certificates, Identifiers, and Profiles.
2. Select Devices.
3. Click Download Sample File for an example file.
4. Customize the example file with your specific device information.
5. Upload the device file.

For more information on multi-device registration, see [`Register multiple devices`](https://developer.apple.comhttps://developer.apple.com/help/account/register-devices/register-multiple-devices).

Add a single device by clicking the plus (+) button next to the Devices title. Specify the identifier and a name for the device. Use a name that makes the device easy to identify; for example, combine the owner’s name and device type, ”Ravi Patel’s iPhone 11”.

You can disable devices that you no longer permit to use your app: select the device and click Disable. Code signing doesn’t include the device while it’s disabled, but the device counts against the number of devices in the product family until your account renewal date. Disabling a device invalidates any provisioning profiles that include the device; automatic signing regenerates the profile the next time you build your app, or you can regenerate the profile manually if you’re not using automatic signing.

##### Update Your Provisioning Profile

When you use automatic signing, Xcode automatically updates the provisioning profile when you export the app.

To use manual signing, sign in to your developer account, select Certificates, Identifiers, and Profiles, then select Profiles. Click the plus sign next to the Profiles header to create a new provisioning profile. Then:

1. Select the type of profile by type and platform.
2. Select your App ID.
3. Select the signing certificate.
4. Select the device or devices to include in the profile.
5. Provide a name for the profile.
6. Select Generate.

You can edit an existing profile and regenerate it to add or remove devices. Once you generate the profile, download it, then drag the downloaded profile to the Xcode dock icon and drop it to install it. You can also download it from Xcode > Settings > Accounts, using the Download Manual Profiles button when you select your account.

##### Configure Code Signing

To allow Xcode to manage signing for you, toggle the Automatically manage signing checkbox from the Signing & Capabilities tab in the project editor and select a Team. To manually sign your app, select a profile to use from the Provisioning Profile dropdown menu. You can also select Import profile or Download profile to add an additional profile from your account.

##### Archive the App

In the main window of your Xcode project, choose a target and a run destination from the Scheme toolbar menu. If you select a simulator for your run destination, Xcode builds an archive matching the build-only device type for that simulator. Choose Product > Archive to build the target and Xcode displays the archive in the Archives organizer.

> **Note**: For an app built with Mac Catalyst, create separate archives for the iPad and Mac Catalyst version. When creating the archive for the Mac Catalyst version, choose the run destination that includes Mac Catalyst in its name. For an app built with Designed for iPad, create a single archive using iPad as the run destination or any run destination that includes Designed for iPad in its name. These run destinations produce the same archive.

##### Export the App

From the archive, export a version of the app to distribute to users:

1. In the Archives organizer, select the archive, then click Distribute App.
2. Select Debugging to prepare a version of your app for debugging on your team’s devices.
3. Click Export and select a location to save the exported app.

For more information on solving issues with code signing, see [`Code Signing Resources`](https://developer.apple.comhttps://developer.apple.com/forums/thread/707080).

##### Install the App on User Devices

When you save the exported app, Xcode creates a folder that contains a few files, including the iOS App file, which is a file with an `.ipa` filename extension. Distribute that file to your users so they can install it on their devices by using Xcode or Apple Configurator 2.

For macOS, double-click the file to install and run it.

To install iOS, iPadOS, tvOS, visionOS, or watchOS apps using Xcode:

1. Attach the device to the computer, or attach the paired phone for a watchOS device.
2. Select Window > Devices and Simulators, and then select the Devices tab.
3. Select the attached device.
4. Click the Add button (+) under the Installed Apps section.
5. Select the iOS App file to install the app.

To install iOS, iPadOS, tvOS, visionOS, or watchOS apps with Apple Configurator 2:

1. Attach the device to your Mac, or attach the paired phone for a watchOS device.
2. Select the attached device.
3. Click the Add button (+).
4. Select the iOS App file to install the app.

> ❗ **Important**: Every time you run your `.ipa`-based app on an iOS or watchOS device, you need to enable Developer Mode on that device. See [`Enabling Developer Mode on a device`](enabling-developer-mode-on-a-device.md) for more information.

## See Also

- [Distributing your app for beta testing and releases](distributing-your-app-for-beta-testing-and-releases.md)
  Release your app to beta testers and users.
- [Packaging Mac software for distribution](packaging-mac-software-for-distribution.md)
  Build a zip archive, disk image, or installer package for distributing your Mac software.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/distributing-your-app-to-registered-devices)*