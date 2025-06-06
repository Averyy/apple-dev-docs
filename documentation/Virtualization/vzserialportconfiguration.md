# VZSerialPortConfiguration

**Framework**: Virtualization  
**Kind**: class

The common configuration traits for serial port requests.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZSerialPortConfiguration
```

#### Overview

Don’t create a [`VZSerialPortConfiguration`](vzserialportconfiguration.md) object directly. Instead, instantiate a concrete instance of one of its subclasses, such as [`VZVirtioConsoleDeviceConfiguration`](vzvirtioconsoledeviceconfiguration.md). Use the [`attachment`](vzserialportconfiguration/attachment.md) property of this class to configure the medium through which serial communication happens.

## Topics

### Configuring the Attachment Point
- [var attachment: VZSerialPortAttachment?](vzserialportconfiguration/attachment.md)
  The object that defines how the configuration of the virtual machine’s serial port interfaces.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZVirtioConsoleDeviceSerialPortConfiguration](vzvirtioconsoledeviceserialportconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioConsoleDeviceSerialPortConfiguration](vzvirtioconsoledeviceserialportconfiguration.md)
  A configuration object that requests the creation of a console device to communicate with the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzserialportconfiguration)*