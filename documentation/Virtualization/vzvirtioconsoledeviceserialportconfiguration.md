# VZVirtioConsoleDeviceSerialPortConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A configuration object that requests the creation of a console device to communicate with the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioConsoleDeviceSerialPortConfiguration
```

```objc
@interface VZVirtioConsoleDeviceSerialPortConfiguration : VZSerialPortConfiguration
```

## Overview

A [`VZVirtioConsoleDeviceSerialPortConfiguration`](./vzvirtioconsoledeviceserialportconfiguration.md) object enables serial communication between the guest operating system and host computer through the Virtio interface. After you create this configuration object, configure its inherited [`attachment`](./vzserialportconfiguration/attachment.md) property with an object that defines the type of serial communication you want to enable. Use a [`VZFileHandleSerialPortAttachment`](./vzfilehandleserialportattachment.md) object to enable two-way communication between the guest and host, and use a [`VZFileSerialPortAttachment`](./vzfileserialportattachment.md) object to enable one-way communication from the guest to the file you designate.

## Topics

### Creating the Configuration Object
- [init()](./vzvirtioconsoledeviceserialportconfiguration/init%28%29.md)
  Creates a serial port configuration object.

## Relationships

### Inherits From
- [VZSerialPortConfiguration](./vzserialportconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configurations
- [class VZSerialPortConfiguration](./vzserialportconfiguration.md)
  The common configuration traits for serial port requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoledeviceserialportconfiguration)*