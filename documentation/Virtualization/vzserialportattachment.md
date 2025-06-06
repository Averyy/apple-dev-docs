# VZSerialPortAttachment

**Framework**: Virtualization  
**Kind**: class

The common behaviors for the serial attachment points of your virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZSerialPortAttachment
```

#### Overview

Don’t create a [`VZSerialPortAttachment`](vzserialportattachment.md) object directly. Instead, instantiate a concrete subclass such as [`VZFileHandleSerialPortAttachment`](vzfilehandleserialportattachment.md) to configure how the virtual machine’s serial port connects with the host computer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZFileHandleSerialPortAttachment](vzfilehandleserialportattachment.md)
- [VZFileSerialPortAttachment](vzfileserialportattachment.md)
- [VZSpiceAgentPortAttachment](vzspiceagentportattachment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZFileHandleSerialPortAttachment](vzfilehandleserialportattachment.md)
  An attachment point that allows bidirectional communication using file handles.
- [class VZFileSerialPortAttachment](vzfileserialportattachment.md)
  An attachment point that writes data from the guest system to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzserialportattachment)*