# Running your app on simulated or physical devices

**Framework**: Xcode

Launch your app on a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a physical device paired with your Mac.

#### Overview

To test your app, build and run it on a simulated or physical device. Use simulated devices to debug your app on a variety of hardware that you might not have access to. Be aware that simulators run within Device Hub on your Mac and don’t replicate the performance or features of a physical device. To verify that your app runs exactly as intended, run it on one or more physical devices.

#### Select a Build Scheme and Run Destination

Before you build and run your app, select a build scheme that includes the target for your app in Xcode. A *scheme* is a collection of project details and settings that tell Xcode how to build and run a product from your project. In the toolbar, choose a scheme from the pop-up menu on the left of the run-destination.

Then choose a simulated or physical device from the run destination pop-up menu. Xcode populates the run destination menu with a list of available devices, including simulators for common hardware and the latest operating systems, based on the scheme that you select. For example, if the scheme contains a watchOS app, Xcode shows only watchOS simulated and physical devices as available run destinations. For a scheme containing a macOS app, or the macOS version of an iPad app, choose My Mac from the run destination pop-up menu.

To add physical devices to the run destination pop-up menu, choose Manage Devices and then use Device Hub to pair devices with your Mac. For more information, see [`Managing your simulated and physical devices in Device Hub`](managing-your-simulated-and-physical-devices-in-device-hub.md).

If you don’t have platform support installed for your target, you can’t build and run your app on a device. To install platform support, click the Get button that appears next to the `Any [Platform] Device` run destination. Alternatively, manage your downloads later in Components settings (see [`Downloading and installing additional Xcode components`](downloading-and-installing-additional-xcode-components.md)).

To learn more about schemes, see [`Customizing the build schemes for a project`](customizing-the-build-schemes-for-a-project.md).

> ❗ **Important**: When running apps in a simulator in Device Hub, some hardware-specific features might not be available. Frameworks that provide access to device-specific features also provide API to tell you when those features are available. Call those APIs and handle the case where a feature isn’t available. To test the feature itself, run your code on a physical device.

#### Run the App

To build and run the app on the selected simulated or physical device, click the Run button in the toolbar or choose Product > Run. View the status of the build in the activity area of the toolbar.

If the build is successful, Xcode runs the app and opens a debugging session in the debug area. Use the controls in the debug area to step through your code, inspect variables, and interact with the debugger. To run the app without the debugger, turn off the Debug executable option in the Info tab of the scheme editor.

If you choose a simulator as a run destination, Device Hub opens a compact window by default that shows your app on a device screen where you can interact with it using your Mac.

![A screenshot of the Device Hub compact window for an Apple Vision Pro simulator running an app launched from Xcode.](/images/com.apple.Xcode/device-hub-compact-view@2x.png)

The first time you run your app on a physical device other than a Mac, Xcode needs to register the device and create a provisioning profile that contains the device. To set up a profile, see [`Set up code signing for physical devices`](running-your-app-on-simulated-or-physical-devices#Set-up-code-signing-for-physical-devices.md). Then Xcode runs the app on the device, and you can interact with your app using both the device and Device Hub. To use Device Hub, select the device in the sidebar and click View Screen in the canvas area.

For more information on interacting with different device types in Device Hub, see  [`Interacting with your app in Device Hub`](interacting-with-your-app-in-device-hub.md) and [`Configuring the environment of a simulated device`](configuring-the-environment-of-a-simulated-device.md).

If Xcode stops building the app because it encounters an error, click the indicators in the activity area to read the error and warning messages in the Issue navigator. If you want Xcode to show all build errors, toggle off “Stop build on first error” under Issues in General settings, then run the app again.

When you’re done testing your app in Device Hub, click the Stop button in the Xcode toolbar.

#### Set Up Code Signing for Physical Devices

If you choose a physical device as the run destination, perform a few additional steps to create a development provisioning profile in Xcode. First, sign in with your Apple Developer Program or personal Apple Account in Xcode > Settings > Apple Accounts.

Then, in the Signing & Capabilities pane of the project editor, click Set Up Signing under Signing if it appears. In the sheet, choose your team from the Team pop-up menu, enter a unique bundle ID ([`CFBundleIdentifier`](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundleidentifier)) in the Bundle Identifier field, and click Set Up. If your bundle ID isn’t unique, Xcode shows a warning at the bottom and inactivates the Set Up button.

![A screenshot of the set up signing sheet that shows the team pop-up menu, Bundle Identifier field, and the Set Up button.](/images/com.apple.Xcode/set-up-signing@2x.png)

If the Set Up Signing button doesn’t appear, toggle “Automatically manage signing” on, assign your project to a team, and enter a bundle ID in the Signing & Capabilities pane instead.

In the toolbar of the project editor, choose the physical device as the run destination. When you enable the “Automatically manage signing” option, Xcode registers the device and creates the development provisioning profile for you. If a Register button appears under Signing, click it to add it to the provisioning profile.

> **Note**: You don’t need to set up signing to run your macOS app on your Mac unless you add capabilities that require provisioning.

For more information on developer accounts, see [`Choosing a Membership`](https://developer.apple.comhttps://developer.apple.com/support/compare-memberships/).

## See Also

- [Creating an Xcode project for an app](creating-an-xcode-project-for-an-app.md)
  Set up a new project to start developing your app.
- [Interacting with previews in the canvas](interacting-with-previews-in-the-canvas.md)
  Use the canvas controls to test your view’s appearance and behavior on different devices and configurations.
- [Adding previews to your interface files](adding-previews-to-your-interface-files.md)
  Write code to test your views on different devices and configurations without needing to run your app.
- [Xcode updates](../updates/xcode.md)
  Learn about important changes to Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices)*