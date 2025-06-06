# VZFileHandleSerialPortAttachment

**Framework**: Virtualization  
**Kind**: class

An attachment point that allows bidirectional communication using file handles.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZFileHandleSerialPortAttachment
```

#### Overview

Use a [`VZFileHandleSerialPortAttachment`](vzfilehandleserialportattachment.md) object to configure a serial port using separate file handles for reading and writing data. In your virtual machine, use the file handles in this object in the following way:

- To send data to the guest operating system, write data to the file handle in the [`fileHandleForReading`](vzfilehandleserialportattachment/filehandleforreading.md) property.
- To receive data from the guest operating system, read data from the file handle in the [`fileHandleForWriting`](vzfilehandleserialportattachment/filehandleforwriting.md) property.

## Topics

### Creating the attachment point
- [init(fileHandleForReading: FileHandle?, fileHandleForWriting: FileHandle?)](vzfilehandleserialportattachment/init(filehandleforreading:filehandleforwriting:).md)
  Creates a serial port attachment object from the specified file handles.
### Getting the file handles
- [var fileHandleForReading: FileHandle?](vzfilehandleserialportattachment/filehandleforreading.md)
  The file handle that the guest operating system uses to read data.
- [var fileHandleForWriting: FileHandle?](vzfilehandleserialportattachment/filehandleforwriting.md)
  The file handle that the guest operating system uses to write data.

## Relationships

### Inherits From
- [VZSerialPortAttachment](vzserialportattachment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZFileSerialPortAttachment](vzfileserialportattachment.md)
  An attachment point that writes data from the guest system to a file.
- [class VZSerialPortAttachment](vzserialportattachment.md)
  The common behaviors for the serial attachment points of your virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfilehandleserialportattachment)*