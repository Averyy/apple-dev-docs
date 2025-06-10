# Sharing data with Simulator

**Framework**: Xcode

Enter text directly in Simulator, or share location data, images, web addresses, files, or data from the clipboard with Simulator.

#### Overview

Some app testing scenarios require location data, specific images, or other data to be present in Simulator. In other cases, such as diagnosing an issue or confirming functionality, it’s useful to capture data from Simulator. Depending on the type of data, there are several methods to get data on your Mac into a simulated device, or to get data from a simulated device to your Mac.

##### Share a Location with Simulator

Send your current location to Simulator from Maps.app on your Mac by clicking the Share button, then select Simulator from the share destination list. Choose the simulated device from the drop-down list. The simulated device updates its location to your current location.

To send a selected location from Maps.app to Simulator, first select a location in Maps.app. Then, click the Share button in the view for the location. Select Simulator from the share destination list, then choose the simulated device from the drop-down list. The simulated device updates its location to the location you shared.

##### Share a Web Address with Simulator

To share a web address with Simulator from your Mac, Control-click a web link, then select Share. Alternatively, open a web link in Safari, then select Share. In the Share menu, select Simulator, then choose a simulated device from the drop-down list. The simulated device opens the web link in Safari.

##### Sync or Share Clipboard Data with Simulator

You can sync Simulator’s clipboard with your Mac, or copy it back and forth.

To sync the Simulator clipboard with the Mac, choose Edit > Automatically Sync Pasteboard. A checkmark indicates that the clipboard is synchronized.

To copy clipboard from Simulator to the Mac, choose Edit > Get Pasteboard.

To copy the clipboard on the Mac to Simulator, choose Edit > Send Pasteboard.

##### Add Images to Photos in Simulator

To put image in Simulator’s Photos app, select one or more images from your Mac, or from Photos.app on your Mac. Drag the images to Simulator. Alternatively, select Share, then select Simulator from the share destination list. Choose the simulated device from the drop-down list. Simulator adds the images and opens Photos to display them.

##### Add Files to Simulator

To add files to Simulator, select one or more files in Finder on your Mac, then click the Share button. Select Simulator from the share destination list. Choose the simulated device from the drop-down list. Simulator opens the Files app, and lets you select where to save the files.

##### Enter Text Using the Macos Keyboard

Enter text as input to the simulated device using the keyboard on your Mac.

To connect your Mac keyboard to the simulated device, select I/O > Keyboard > Connect Hardware Keyboard.

To show or hide the onscreen keyboard when a hardware keyboard is connected to the device, choose I/O > Keyboard > Toggle Software Keyboard.

To synchronize the iOS and Mac keyboard languages, select I/O > Keyboard > Use the Same Keyboard Language as macOS.

> **Note**: For Simulator to automatically switch keyboard languages when the Mac layout is changed, select both Connect Hardware Keyboard and Use the Same Keyboard Language as macOS.

##### Use Game Controller Input

For a visionOS simulator, you can share the input from a game controller connected to your Mac.

To connect your Mac game controller to an app running in the simulated device, select I/O > Input > Send Game Controller to Device.

## See Also

- [Testing in Simulator versus testing on hardware devices](testing-in-simulator-versus-testing-on-hardware-devices.md)
  Review the differences between Simulator and hardware devices to determine which you should choose to test a scenario.
- [Testing complex hardware device scenarios in Simulator](testing-complex-hardware-device-scenarios-in-simulator.md)
  Test hardware device-specific scenarios, such as Face ID or Touch ID authentication, fall detection, getting a memory warning, or location changes.
- [Identifying graphics and animations issues in Simulator](identifying-graphics-and-animations-issues-in-simulator.md)
  Reveal performance and display issues in your views with color overlays, and slow down animations to debug and improve them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/sharing-data-with-simulator)*