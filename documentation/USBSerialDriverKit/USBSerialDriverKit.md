# USBSerialDriverKit

**Framework**: USBSerialDriverKit  
**Kind**: module

Develop drivers for serial USB devices connected to your Mac.

**Availability**:
- DriverKit 19.0+

#### Overview

Use the USBSerialDriverKit framework to develop drivers that communicate with USB devices using serial protocols. This framework augments the behavior of the [`SerialDriverKit`](https://developer.apple.com/documentation/SerialDriverKit) framework by configuring the buffers and endpoints needed to transfer data to and from the device. You handle the initial configuration of your device, and the framework manages the transfer of data to and from that device.

Package your driver in an app that uses the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade the driver on the user’s Mac.

> **Note**:  USBSerialDriverKit is available on macOS.

## Topics

### Samples
- [DriverKit sample code](../DriverKit/driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Serial USB Interface
- [com.apple.developer.driverkit.family.serial](../BundleResources/Entitlements/com.apple.developer.driverkit.family.serial.md)
  A Boolean value that indicates whether to match the driver against devices with serial communication interfaces.
- [IOUserUSBSerial](iouserusbserial.md)
  A service that manages a serial connection to a USB device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/USBSerialDriverKit)*