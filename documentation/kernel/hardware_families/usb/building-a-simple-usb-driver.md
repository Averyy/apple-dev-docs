# Building a Simple USB Driver

**Framework**: Kernel

Set up and load a driver that logs output to the Console app.

**Availability**:
- macOS 10.15+
- Xcode 12.0+

#### Overview

This code project builds a simple USB driver. The driver logs events to the Console and responds to interrupts, such as when the user inserts or removes a device. Because it is a template driver with limited functionality, it can be used as a starting point for a more sophisticated driver.

##### 3696665

To run the sample code project in Xcode, make sure to use macOS 10.15.5 or later and Xcode 11.5 or later.

For the driver to load, System Integrity Protection (SIP) must be off. For more information on this process, see [`Disabling and Enabling System Integrity Protection`](https://developer.apple.com/documentation/security/disabling-and-enabling-system-integrity-protection).

##### 3696666

This sample USB driver works by detecting when a USB device is plugged into a Mac and logging the event. The test device should be unsupported under macOS; otherwise, an existing driver will take precedence, recognize the device, and preempt this sample driver.

The driver detects the device based on a number of critiera inside of the Info.plist’s `IOKitPersonalities > SimpleUSBInterfaceDriver` section, including configuration value, interface number, product identifier, and vendor identifier.

The sample driver requires the following command to find criteria that matches the keys in the Info.plist file for a selected USB device plugged into a Mac:

```swift
ioreg -w0 -rc IOUSBHostInterface -l
```

WIth the device’s parmeters identified and placed in the Info.plist file, the driver loads and intializes the device upon insertion.

##### 3696667

At build time, Xcode runs the “Launch Terminal” run script build phase, which launches the Terminal app in the directory where the newly-built driver resides.

The following commands copy the the driver into the home folder, change the current directory to that location, set ownership and permissions, and load the driver.

```swift
sudo cp -R SimpleUSBInterfaceDriver.kext ~
cd ~
sudo chown -R root:wheel SimpleUSBInterfaceDriver.kext
sudo chmod -R 755 SimpleUSBInterfaceDriver.kext
sudo kextload SimpleUSBInterfaceDriver.kext
```

The kernel loads the driver and communicates the status through the logging system. The Console app shows the logging messages.

##### 3696668

When testing completes, the following command directs the kernel to unload the driver:

```swift
sudo kextunload SimpleUSBInterfaceDriver.kext
```

It is important to re-enable SIP once driver testing completes. Failure to re-enable SIP leaves the computer vulnerable to malicious code. See [`Disabling and Enabling System Integrity Protection`](https://developer.apple.com/documentation/security/disabling-and-enabling-system-integrity-protection) for more information.

## See Also

- [IOUSBHostIOSourceClientRecordLink](iousbhostiosourceclientrecordlink.md)
  A structure that represents a USB host input/output source client record entry.
- [IOUSBHostIOSourceClientRecordList](iousbhostiosourceclientrecordlist.md)
  A structure that represents a list of USB host input/output source client records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/usb/building_a_simple_usb_driver)*