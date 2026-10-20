# VZSerialPortAttachment

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The common behaviors for the serial attachment points of your virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZSerialPortAttachment
```

```objc
@interface VZSerialPortAttachment : NSObject
```

#### Overview

Don’t create a [`VZSerialPortAttachment`](./vzserialportattachment.md) object directly. Instead, instantiate a concrete subclass such as [`VZFileHandleSerialPortAttachment`](./vzfilehandleserialportattachment.md) to configure how the virtual machine’s serial port connects with the host computer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZFileHandleSerialPortAttachment](./vzfilehandleserialportattachment.md)
- [VZFileSerialPortAttachment](./vzfileserialportattachment.md)
- [VZSpiceAgentPortAttachment](./vzspiceagentportattachment.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Attachment points
- [class VZFileHandleSerialPortAttachment](./vzfilehandleserialportattachment.md)
  An attachment point that allows bidirectional communication using file handles.
- [class VZFileSerialPortAttachment](./vzfileserialportattachment.md)
  An attachment point that writes data from the guest system to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzserialportattachment)*