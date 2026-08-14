# IOKit

**Framework**: IOKit

Access hardware devices and drivers from your apps and services.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 1.0+

#### Overview

The IOKit framework implements nonkernel access to IOKit objects such drivers and nubs through the device-interface mechanism.

> ❗ **Important**: Devices supported on macOS 11 and later require [`DriverKit`](https://developer.apple.com/documentation/driverkit). Use IOKit in your apps and services to discover and use devices. 

## Topics

### Serial Ports
- [Communicating with a Modem on a Serial Port](communicating_with_a_modem_on_a_serial_port.md)
  Find and connect to a modem attached to a serial port using IOKit.
### Reference
- [IODataQueueClient.h](iodataqueueclient_h.md)
- [IOKitLib.h](iokitlib_h.md)
- [IOTypes.h User-Space](iotypes_h_user-space.md)
- [IOKit Structures](iokit_structures.md)
- [IOKit Enumerations](iokit_enumerations.md)
- [IOKit Constants](iokit_constants.md)
- [IOKit Functions](iokit_functions.md)
- [IOKit Data Types](iokit_data_types.md)

## See Also

- [IOKit Fundamentals](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/IOKitFundamentals/Introduction/Introduction.html#//apple_ref/doc/uid/TP0000011)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit)*