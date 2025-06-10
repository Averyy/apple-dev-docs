# Adding additional simulators

**Framework**: Safari Developer Features

Add simulators for different devices and iOS versions to use for web development.

#### Overview

A Simulator runtime is an OS package that Simulator loads when booting a device, which is specific to a particular OS and version. Simulator runtimes are then used by numerous different Simulators with different device types, like iPhone 16 or iPad Pro.

If you want to test on another platform or OS version, you need to add the Simulator runtime for that platform, and then create a new Simulator.

#### Install and Uninstall Simulator Runtimes

##### Adding a Simulator Runtime

1. In Xcode, from the menu bar, choose  > .
2. Go to the  tab.
3. The Platform Support section shows the latest versions of available platform and Simulator runtimes. Click the  button next to the one you need.
4. If you need a previously released Simulator runtime, click the Add button () in the lower left corner, and then select a platform to view a list of available versions.
5. Select a version and click .

##### Removing a Simulator Runtime

To recover storage space from unused Simulator runtimes:

1. In Xcode, from the menu bar, choose  > .
2. Go to the  tab.
3. Select the Simulator runtime you wish to remove.
4. Click the Delete button () in the lower left corner.
5. Click  in the confirmation dialog.

#### Add and Remove Simulators

##### Adding a Simulator

1. In Xcode, from the menu bar, choose  > .
2. Choose  at the top of the sidebar.
3. Click the Add button () in the lower left corner.
4. Choose a  and  for your simulator, and optionally provide it with a name.
5. Click  to create the new simulator.

##### Removing a Simulator

1. In Xcode, from the menu bar, choose  > .
2. Choose  at the top of the sidebar.
3. Control-click on the Simulator you wish to remove.
4. Choose  from the pop-up menu.
5. Click  in the confirmation dialog.

> 💡 **Tip**: Simulators can also be [`managed from the terminal`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/installing-additional-simulator-runtimes#Install-and-manage-Simulator-runtimes-from-the-command-line).

## See Also

- [Installing Xcode and Simulators](installing-xcode-and-simulators.md)
  Install simulators to use for web development.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/adding-additional-simulators)*