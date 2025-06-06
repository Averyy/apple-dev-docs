# USBDriverKit

**Framework**: Usbdriverkit  
**Kind**: module

Develop drivers for USB-based devices.

**Availability**:
- DriverKit 19.0+

#### Overview

Use the [`USBDriverKit`](USBDriverKit.md) framework to develop drivers for custom or non-class-compliant USB devices for use with macOS. The objects in this framework serve as providers for your driver. Use them as is to access the device configurations, interfaces, and endpoints of the USB device. Each object provides methods for fetching any needed descriptors from the USB device, and for initiating requests to perform your driver’s custom behaviors.

Develop your driver by subclassing [`IOService`](https://developer.apple.com/documentation/DriverKit/IOService) in the [`DriverKit`](https://developer.apple.com/documentation/DriverKit) framework. On macOS, use the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade your driver. On iPadOS, the system automatically discovers and upgrades drivers along with their host apps.

> **Note**:  USBDriverKit is available on macOS for Intel and Apple Silicon devices, and on iPadOS for devices with an M-series chip.

## Topics

### Essentials
- [com.apple.developer.driverkit.transport.usb](../BundleResources/Entitlements/com.apple.developer.driverkit.transport.usb.md)
  An array of dictionaries that identify the USB devices the driver supports.
### Samples
- [DriverKit sample code](../DriverKit/driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Providers
- [IOUSBHostInterface](iousbhostinterface.md)
  A provider object that manages interactions with an interface of the USB device.
- [IOUSBHostDevice](iousbhostdevice.md)
  A provider object that represents the USB device.
### Endpoint Communication
- [IOUSBHostPipe](iousbhostpipe.md)
  An object you use to transfer data to or from a USB endpoint.
### USB Specifications
- [USB Device Descriptors](usb-device-descriptors.md)
  Determine the capabilities and configuration of a device using descriptors from the USB specification.
- [Additional Specifications](additional-specifications.md)
  Request information from a device and get hardware and timing information.
- [Registry Property Names](registry-property-names.md)
  Search for specific keys in the device registry.
- [Utilities](utilities.md)
  Manipulate bit structures and convert integers between device- and platform-native formats.
### References
- [USBDriverKit Enumerations](usbdriverkit-enumerations.md)
- [USBDriverKit Functions](usbdriverkit-functions.md)
- [USBDriverKit Data Types](usbdriverkit-data-types.md)
- [USBDriverKit Macros](usbdriverkit-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/USBDriverKit)*