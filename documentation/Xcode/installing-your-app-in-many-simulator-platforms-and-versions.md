# Installing your app in many Simulator platforms and versions

**Framework**: Xcode

Set up your app in multiple Simulator platforms and versions without the build-and-run cycle.

#### Overview

When you’re ready to test your app in different devices to confirm that it handles screen size and other environmental differences correctly, you could select each Simulator run destination that you want and then choose Product > Run to install your app in that Simulator run destination. When you test across several Simulator run destinations at the same time, that can be time consuming. Instead, install your app in multiple target Simulator run destinations using drag and drop or share.

##### Prepare Your App for Installation

Build your app so that you have a product you can install in a simulated device. To build your app:

1. In Xcode, select a build scheme and Simulator run destination.
2. Choose Product > Build.

For more information on building and running your app in Simulator, see [`Running your app in Simulator or on a device`](running-your-app-in-simulator-or-on-a-device.md).

##### Install Your App with Drag and Drop or Share

First, launch each device variant you want to install your app into in Simulator. Choose File > Open Simulator, and select a device variant.

Then, navigate to the built product in Finder. In Xcode, choose Product > Show Build Folder in Finder, then select the Products folder in the Finder window that Xcode displays. Select the folder for the build scheme and destination for which you built the product, then select your application file.

Drag the application bundle over a Simulator window to install your app in that simulated device.

Alternatively, use share to install your app:

1. Control-click your application file and select Share…
2. Choose Simulator from the list of sharing options.
3. From the Choose Simulator drop-down, choose All Simulators to install your app in each open device, or choose a specific device.
4. Click Send to install your app in the selected Simulator.

## See Also

- [Downloading and installing additional Xcode components](downloading-and-installing-additional-xcode-components.md)
  Add more Simulator runtimes, optional features, and support for additional platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/installing-your-app-in-many-simulator-platforms-and-versions)*