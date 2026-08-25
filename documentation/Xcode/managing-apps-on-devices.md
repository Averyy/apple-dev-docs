# Managing apps on devices

**Framework**: Xcode

Find, add, and remove apps installed for testing on simulated and physical devices.

#### Overview

Use the Apps inspector in Device Hub to view, install, and remove apps on both simulated and physical devices. During development, Xcode installs your app on devices for you (see [`Running your app on simulated or physical devices`](running-your-app-on-simulated-or-physical-devices.md)), and you remove it using Device Hub. Later, when you’re ready to distribute your app for testing (see [`Distributing your app to registered devices`](distributing-your-app-to-registered-devices.md)), you can use Device Hub independently of Xcode to add and remove apps on multiple test devices.

![A screenshot of the Device Hub with a simulator selected in the sidebar on the left, an iPhone simulator running in the canvas in the middle, and the Apps inspector showing an installed app selected on the right.](/images/com.apple.Xcode/device-hub-apps-inspector@2x.png)

#### View Apps on Devices

To find all apps on a device:

1. Select the device in the sidebar.
2. Click Apps in the inspector’s toolbar.
3. If your apps don’t appear, follow the steps in the inspector to show the apps on the device. For example, click Start in the canvas for simulators.

Then use the controls at the bottom of the table to quickly find an app. Enter a search string in the Filter text field, then choose an option, such as Developer, from the pop-up menu to the right.

#### Install Apps on Devices

To install iOS, iPadOS, tvOS, visionOS, or watchOS apps on a device without using Xcode:

1. In the Apps inspector, click the Add button (+) below the list of apps.
2. Select the iOS Package Archive file (with an `.ipa` extension) and click Open.

Alternatively, use Apple Configurator to install apps on devices. For more information, see [`Apple Configurator Support`](https://developer.apple.comhttps://support.apple.com/apple-configurator).

To install a macOS app, drag the app bundle (with an `.app` extension) to the `/Applications` folder or another folder of your choice on your Mac.

#### Remove Apps From Devices

To remove iOS, iPadOS, tvOS, visionOS, or watchOS apps from a device:

1. In the Apps inspector, select one or more apps from the list.
2. Click the Remove button (-) under the list of apps.

To delete a macOS app, drag the app (with an `.app` extension) to the Trash in Finder.

## See Also

- [Locating device identifiers](locating-device-identifiers.md)
  Get the unique identifier for a device before registering it in your developer account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/managing-apps-on-devices)*